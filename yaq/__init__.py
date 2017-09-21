"""Yet another acquisition."""


# --- import -------------------------------------------------------------------------------------


import sys
import os


# --- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


# --- version ------------------------------------------------------------------------------------


# read from VERSION file
with open(os.path.join(os.path.dirname(here), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

# add git branch, if appropriate
directory = os.path.dirname(os.path.dirname(here))
p = os.path.join(directory, '.git', 'HEAD')
if os.path.isfile(p):
    with open(p) as f:
        __branch__ = f.readline().rstrip().split(r'/')[-1]
    if __branch__ != 'master':
        __version__ += '-' + __branch__
else:
    __branch__ = None
