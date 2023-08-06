"""Python RunStats - Online Statistics and Regression

"""

try:
    from .fast import Statistics, Regression
    __compiled__ = True
except ImportError:
    from .core import Statistics, Regression
    __compiled__ = False

__title__ = 'runstats'
__version__ = '1.7.1'
__build__ = 0x010701
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015-2017 Grant Jenks'
