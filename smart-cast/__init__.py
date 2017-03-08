#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace requests_mv_integrations

__title__ = 'safecast'
__version__ = '0.00.5'
__build__ = 0x000005
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'

__python_required_version__ = (3, 0)


def safe_cast(val, to_type, default=None):
    """Safely cast value to type, and if failed, returned default.

    Args:
        val:
        to_type:
        default:

    Returns:

    """
    if val is None:
        return default

    try:
        return to_type(val)
    except ValueError:
        return default


def safe_str(val):
    """Safely cast value to str

    Args:
        val:

    Returns:

    """
    return safe_cast(val, str, "")


def safe_float(val, ndigits=2):
    """Safely cast value to float

    Args:
        val:

    Returns:

    """
    return round(safe_cast(val, float, 0.0), ndigits)


def safe_int(val):
    """Safely cast value to int

    Args:
        val:

    Returns:

    """
    return safe_cast(safe_float(val, 0), int, 0)


def safe_dict(val):
    """Safely cast value to dict

    Args:
        val:

    Returns:

    """
    return safe_cast(val, dict, {})