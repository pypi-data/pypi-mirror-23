from __future__ import absolute_import as _absolute_import

from pkg_resources import DistributionNotFound as _DistributionNotFound
from pkg_resources import get_distribution as _get_distribution

from .ndarray_listener import ndarray_listener

try:
    __version__ = _get_distribution('ndarray_listener').version
except _DistributionNotFound:
    __version__ = 'unknown'


def test():
    import os
    p = __import__('ndarray_listener').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q', '--doctest-modules'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code
