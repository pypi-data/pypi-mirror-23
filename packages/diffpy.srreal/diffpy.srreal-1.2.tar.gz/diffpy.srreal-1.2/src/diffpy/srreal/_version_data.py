#!/usr/bin/env python
##############################################################################
#
# diffpy.srreal     by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2008 The Trustees of Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
##############################################################################


"""Extraction of version data for diffpy.srreal package

Does not import any extension module unlike the standard version.
"""

from pkg_resources import resource_filename

import sys
if sys.version_info[0] >= 3:
    from configparser import RawConfigParser
else:
    from ConfigParser import RawConfigParser
del sys

# obtain version information from the version.cfg file
cp = RawConfigParser(dict(version='', date='', commit='', timestamp=0))
if not cp.read(resource_filename(__name__, 'version.cfg')):
    from warnings import warn
    warn('Package metadata not found, execute "./setup.py egg_info".')

__version__ = cp.get('DEFAULT', 'version')
__date__ = cp.get('DEFAULT', 'date')
__gitsha__ = cp.get('DEFAULT', 'commit')
__timestamp__ = cp.getint('DEFAULT', 'timestamp')

del cp

# End of file
