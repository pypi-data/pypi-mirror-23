import os
import re
import ast
from six.moves.configparser import ConfigParser as Config
from .logging import logger


class ConfigError(Exception):
    """Configuration parsing error."""
    pass


def read_config(*locations):
    """
    Reads and parses the given configuration files.
    
    :param locations: the input configuration file paths
    :return: the configuration
    :rtype: :class:`qiutil.ast_config.ASTConfig`
    :raise IOError: if no configuration files could not be read
    """
    cfg = ASTConfig()
    locations = [os.path.abspath(path) for path in locations]
    cfg_files = cfg.read(locations)
    if not cfg_files:
        raise ConfigError(
            "Configuration files could not be read: %s" % locations)
    logger(__name__).debug("Loaded configuration from %s with sections %s." %
          (cfg_files, cfg.sections()))
    
    return cfg


class ASTConfig(Config):
    """
    ASTConfig parses a configuration file with AST property values as
    follows:
    
    * An unquoted digits value is parsed as an integer.
    
    * An unquoted digits value with a single period is parsed as a float.
    
    * A ``[]`` bracketed value is parsed as a list.
    
    * A ``()`` bracketed value is parsed as a tuple.
    
    * A ``{}`` bracketed value is parsed as a dictionary.
    
    * A case-insensitive match on ``true`` or ``false`` is parsed
      as the Python object ``True``, resp. ``False``.
    
    * A case-insensitive match on ``none``, ``null`` or ``nil`` is
      parsed as the Python ``None`` object.
    
    * All other values are parsed as string.
    
    For example, given the configuration file ``tuning.cfg`` with content::
        
        [Tuning]
        method = FFT
        iterations = [[1, 2], 5]
        parameters = [(1,), (2, 3), -0.4]
        two_tailed = false
        threshold = 4.0
        plugin_args = {'qsub_args': '-pe mpi 48-120'}
    
    then::
        
        >>> cfg = ASTConfig('tuning.cfg')
        >>> cfg['Tuning']
        {'method': u'FFT', 'parameters' = [(1,), (2, 3), -0.4],
         'iterations': [[1, 2], 5],
         'two_tailed': False, 'threshold': 4.0,
         'plugin_args': {'qsub_args': '-pe mpi 48-120'}}
    """
    
    COLL_PAT = """
        \%(left)s   # The left delimiter
        (.*)        # The list items
        \%(right)s$ # The right delimiter
        """
    """A bunch string pattern."""
    
    LIST_PAT = re.compile(COLL_PAT % dict(left='[', right=']'), re.VERBOSE)
    """A list string pattern."""
    
    TUPLE_PAT = re.compile(COLL_PAT % dict(left='(', right=')'), re.VERBOSE)
    """A tuple string pattern."""
    
    DICT_PAT = re.compile(COLL_PAT % dict(left='{', right='}'), re.VERBOSE)
    """A dictionary string pattern."""
    
    EMBEDDED_COLL_PAT = """
        ([^%(left)s]*)          # A prefix without the left delimiter
        (\%(left)s.*\%(right)s)? # The embedded item
        ([^%(right)s]*)         # A suffix without the right delimiter
        $                       # The end of the value
    """
    
    EMBEDDED_LIST_PAT = re.compile(EMBEDDED_COLL_PAT %
                                   dict(left='[', right=']'), re.VERBOSE)
    """A (prefix)(list)(suffix) recognition pattern."""
    
    EMBEDDED_TUPLE_PAT = re.compile(EMBEDDED_COLL_PAT %
                                    dict(left='(', right=')'), re.VERBOSE)
    """A (prefix)(tuple)(suffix) recognition pattern."""
    
    EMBEDDED_DICT_PAT = re.compile(EMBEDDED_COLL_PAT %
                                   dict(left='{', right='}'), re.VERBOSE)
    """A (prefix)(dictionary)(suffix) recognition pattern."""
    
    PARSEABLE_ITEM_PAT = re.compile("""
        (
            True              # The True literal
            | False           # The False literal
            | -?\.\d+         # A decimal with leading period
            | -?\d+(\.\d*)?   # A number
            | -?\d+(\.\d*)?e[+-]\d+ # A floating point
            | \'.*\'          # A single-quoted string
            | \".*\"          # A double-quoted string
        )$                    # The end of the value
        """, re.VERBOSE)
    """A non-list string parseable by AST."""
    
    def __iter__(self):
        """
        :yield: the next *(section, {item: value})* tuple
        """
        for s in self.sections():
            yield (s, self[s])
    
    def __contains__(self, section):
        """
        :param: the config section to find
        :return: whether this config has the given section
        """
        return self.has_section(section)
    
    def __getitem__(self, section):
        """
        :param section: the configuration section name
        :return: the section option => value dictionary
        """
        return {name: self._parse_entry(name, value)
                for name, value in self.items(section)}
    
    def _parse_entry(self, name, s):
        """
        :param name: the option name
        :param s: the option string value to parse
        :return: the parsed AST value
        :raise SyntaxError: if the value cannot be parsed
        """
        if s:
            ast_value = self._to_ast(s)
            try:
                return ast.literal_eval(ast_value)
            except Exception:
                logger(__name__).error("Cannot load the configuration entry"
                                       " %s: %s parsed as %s" % (name, s, ast_value))
                raise
    
    def _to_ast(self, s):
        """
        :param s: the input string
        :return: the equivalent AST string
        """
        # Trivial case.
        if not s:
            return
        # If the input is a boolean, number or already quoted,
        # then we are done.
        if ASTConfig.PARSEABLE_ITEM_PAT.match(s):
            return s
        
        # If the string is a list, then make a quoted list.
        # Otherwise, if the string signifies a boolean, then return the boolean.
        # Otherwise, quote the content.
        if self._is_bunch(s):
            return self._quote_bunch(s)
        s_lc = s.lower()
        if s_lc == 'true':
            return 'True'
        elif s_lc == 'false':
            return 'False'
        elif s_lc in ['none', 'null', 'nil']:
            return 'None'
        else:
            return '"%s"' % s.replace('"', '\\"')
    
    def _is_bunch(self, s):
        return (ASTConfig.LIST_PAT.match(s) or
                ASTConfig.TUPLE_PAT.match(s) or
                ASTConfig.DICT_PAT.match(s))
    
    def _quote_bunch(self, s):
        # A dictionary must already be properly quoted.
        if s[0] == '{':
            return s
        quoted_items = self._quote_bunch_content(s[1:-1])
        if len(quoted_items) == 1:
            quoted_items.append('')
        return s[0] + ', '.join(quoted_items) + s[-1]
    
    def _quote_bunch_content(self, s):
        """
        :param s: the comma-separated items
        :return: the bunch of quoted items
        """
        pre, mid, post = ASTConfig.EMBEDDED_LIST_PAT.match(s).groups()
        if not mid:
            pre, mid, post = ASTConfig.EMBEDDED_TUPLE_PAT.match(s).groups()
        if not mid:
            pre, mid, post = ASTConfig.EMBEDDED_DICT_PAT.match(s).groups()
        if mid:
            items = []
            if pre:
                items.extend(self._quote_bunch_content(pre))
            # Balance the left and right delimiter.
            left = mid[0]
            right = mid[-1]
            count = 1
            i = 1
            while (count > 0):
                if mid[i] == left:
                    count = count + 1
                elif mid[i] == right:
                    count = count - 1
                i = i + 1
            post = mid[i:] + post
            mid = mid[0:i]
            items.append(self._quote_bunch(mid))
            if post:
                items.extend(self._quote_bunch_content(post))
            return items
        else:
            # No embedded bunch.
            items = re.split('\s*,\s*', s)
            quoted_items = [self._to_ast(item) for item in items if item]
            return quoted_items
