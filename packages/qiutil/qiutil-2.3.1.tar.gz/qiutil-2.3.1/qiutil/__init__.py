"""The Quantitative Imaging utility module."""

__version__ = '2.3.1'
"""
The *major*\ .\ *minor*\ .\ *patch* version.
The verson numbering scheme is described in
`Fast and Loose Versioning <https://gist.github.com/FredLoney/6d946112e0b0f2fc4b57>`_
"""

# Import collections, file and logging, since these are also
# standard Python libraries. This import allows the client to
# use the nested modules directly, e.g.:
#   with qiutil.file.open(...):
# rather than:
#   from qiutil import file
#   with file.open(...): # Misleading
#  or:
#   from qiutil import file as qifile
#   with qifile.open(...): # Awkward
#
# Import command as well, since it is a common module name.
from . import (collections, command, file, logging)
