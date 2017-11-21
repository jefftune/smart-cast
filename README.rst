.. -*- mode: rst -*-


safe-cast
---------

Cast data in Python safely.


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |license|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions|

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0

.. |travis| image:: https://travis-ci.org/TuneLab/safe-cast.svg?branch=master
    :target: https://travis-ci.org/TuneLab/safe-cast

.. |coveralls| image:: https://coveralls.io/repos/github/TuneLab/safe-cast/badge.svg?branch=master
    :alt: Code Coverage Status
    :target: https://coveralls.io/github/TuneLab/safe-cast?branch=master

.. |requires| image:: https://requires.io/github/TuneLab/safe-cast/requirements.svg?branch=master
     :target: https://requires.io/github/TuneLab/safe-cast/requirements/?branch=master
     :alt: Requirements Status

.. |version| image:: https://img.shields.io/pypi/v/safe-cast.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/safe-cast

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/safe-cast.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/safe-cast

.. end-badges


Functions
---------

+-----------------------------------------------+------------------------------------------------------------------+
| Function                                      | Purpose                                                          |
+===============================================+==================================================================+
| ``safe_cast(val, to_type, default=None)``     | Cast value to requested type, if failed, then used default.      |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_str(val, default=None)``               | Cast value to type string, if failed, then used default.         |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_float(val, ndigits=2, default=None)``  | Cast value to type float, if failed, then used default.          |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_int(val, default=None)``               | Cast value to type int, if failed, then used default.            |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_dict(val, default=None)``              | Cast value to type dictionary, if failed, then used default.     |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_smart_cast(val)``                      | Determine type based upon value, and cast to that type.          |
+-----------------------------------------------+------------------------------------------------------------------+
| ``safe_cost(val)``                            | Cast value to type float by 4 decimal points.                    |
+-----------------------------------------------+------------------------------------------------------------------+

