import __builtin__
import os
import glob
import re
import inspect
import gzip
import scandir
from contextlib import contextmanager
from .uid import generate_string_uid

SPLITEXT_PAT = re.compile("""
    (.*?)           # The file path without the extension
    (               # The extension group
      (\.\w+)+      # The (possibly composite) extension
    )?              # The extension is optional
    $               # Anchor to the end of the file path
    """, re.VERBOSE)
"""
Regexp pattern that splits the name and extension.

:see: :meth:`splitexts`
"""


class FileError(Exception):
    pass

@contextmanager
def open(filename):
    """
    Opens the given file. If the file extension ends in ``.gz``,
    then the content is uncompressed.

    :param filename: the file path
    :return: the file input stream
    :raise: IOError if the file cannot be read
    """
    _, ext = os.path.splitext(filename)
    # The gzip or normal file open context function.
    if ext == '.gz':
        context = gzip.open
    else:
        context = __builtin__.open

    # Open the file.
    with context(filename) as fp:
        yield fp


def splitexts(location):
    """
    Splits the given file path into a name and extension.
    Unlike ``os.path.splitext``, the resulting extension can be composite.

    Example:

    >>> import os
    >>> os.path.splitext('/tmp/foo.nii.gz')
    ('/tmp/foo.nii', '.gz')
    >>> from qiutil.file import splitexts
    >>> splitexts('/tmp/foo.3/bar.nii.gz')
    ('/tmp/foo.3/bar', '.nii.gz')

    :param location: the file path
    :return: the *(prefix, extensions)* tuple
    """
    matches = SPLITEXT_PAT.match(location).groups()[:2]
    # Pad with an empty extension, if necessary.
    matches += (None,) * (2 - len(matches))

    return tuple(matches)


def splitboth(location):
    """
    Splits the given file path into a directory, name and extension.
    Unlike ``os.path.splitext``, the resulting extension can be
    composite.

    Example:

    >>> import os
    >>> from qiutil.file import splitall
    >>> splitall('/tmp/foo.nii.gz')
    ('/tmp', 'foo', '.nii.gz')

    :param location: the file path
    :return: the *(directory, prefix, extensions)* tuple
    """
    prefix, exts = splitexts(location)
    dir_path, base = os.path.split(prefix)
    if dir_path == '':
        dir_path = None

    return (dir_path, base, exts)


def generate_file_name(ext=None):
    """
    Makes a valid file name which is unique to within one microsecond of calling
    this function. The file name is ten characters long without the extension.

    :param ext: the optional file extension, with leading period delimiter
    :return: the file name
    """
    fname = generate_string_uid()
    if ext:
        return fname + ext
    else:
        return fname


class Finder(object):
    """
    Finder matches a file name glob pattern and regular expression.
    """

    def __init__(self, glob='*', regex='.*'):
        """
        :param glob: the glob pattern string
        :param regex: the :class:`RegExp` object or pattern string
        """
        self.glob = glob or '*'
        """The glob pattern string (default ``*``)."""

        if isinstance(regex, str):
            regex = re.compile(regex)
        self.regex = regex or '.*'
        """The file match regular expression (default ``.*``)."""

    def find(self, base_dir=None):
        """
        Iterates over the files which match both the :attr:`glob` and the
        :attr:`regex`. Each iteration result is an absolute file path.

        :param: the parent base directory path (default current directory)
        :yield: the next matching absolute file path
        """
        if not base_dir:
            base_dir = os.getcwd()
        abs_dir = os.path.abspath(base_dir)
        for match in self.match(base_dir):
            yield os.path.join(abs_dir, match.group(0))

    def match(self, base_dir=None):
        """
        Iterates over the files which match both the :attr:`glob` and the
        :attr:`regex`. The match result does not include the base
        directory.

        :param: the parent base directory path (default current directory)
        :yield: the next match
        """
        if not base_dir:
            base_dir = os.getcwd()
        # The primary glob match.
        files = glob.iglob('/'.join((base_dir, self.glob)))
        # Apply the secondary regex filter.
        prefix_len = len(base_dir) + 1
        for location in files:
            # Chop off the base directory prefix.
            rel_path = location[prefix_len:]
            # Match on the rest of the file path.
            match = self.regex.match(rel_path)
            if match:
                yield match


class FileIterator(object):
    """
    FileIterator is a generator class which iterates over the files contained
    recursively in the initializer *filespecs* parameters.
    """

    def __init__(self, *filespecs):
        """
        :param filespecs: the files, directories or file generators over which
            to iterate
        """
        self._filespecs = filespecs

    def __iter__(self):
        """
        Iterates over the files as follows:

        - If the current file specification is a file object, then yield that
          file object.

        - If the current file specification is a non-directory file path,
          then yield that file path.

        - If the current file specification is a directory, then yield each file
          contained recursively in that directory.

        - If the current file specification is a generator, then yield each
          generated item

        :yield: the next file object or path
        :raise FileError: if an iterated file path is neither a directory nor file
        :raise FileError: if an iterated item is not a file object, path
            or generator
        """
        for spec in self._filespecs:
            if isinstance(spec, file):
                yield spec
            elif isinstance(spec, str):
                if os.path.isfile(spec):
                    yield spec
                elif os.path.isdir(spec):
                    for root, dirs, files in scandir.walk(spec):
                        for f in files:
                            yield os.path.join(root, f)
                else:
                    raise FileError("File not found: %s" % spec)
            elif inspect.isgenerator(spec):
                for f in spec:
                    yield f
            else:
                raise FileError("File iteration item is not supported:"
                                 " %s" % spec.__class__)
