.. contents::
   :backlinks: top

========
 Status
========
|VersionsBadge| |ImplementationBadge| |LicenseBadge|

|PyPI| |RTD| |Appveyor| |Travis| |Coveralls| |Codecov| |Codacy| |Scrutinizer|

|Requires| |Pyup|

=======
 About
=======
This is a Python cffi_ port of libtcod_.

This library is `hosted on GitHub <https://github.com/HexDecimal/libtcod-cffi>`_.

Any issues you have with this module can be reported at the
`GitHub issue tracker <https://github.com/HexDecimal/libtcod-cffi/issues>`_.

The latest documentation can be found
`here <https://libtcod-cffi.readthedocs.io/en/latest/>`_.

This project was spun off from the python-tdl_ project,
and is now it's own module.

==============
 Installation
==============
The recommended way to install is by using pip_.

With Python installed, run the following command to install libtcod-cffi::

    python -m pip install libtcod-cffi

This is good enough for most Python installations.
See the requirements section if you're building from source.

=======
 Usage
=======
This module was designed to be backward compatible with the original libtcod
module that is distributed with libtcod.
If you had code that runs on the original module you can use this library as a
drop-in replacement like this::

    import tcod as libtcod

Guides and Tutorials for the original library should also work with this one.

==============
 Requirements
==============
* Python 2.7+, Python 3.4+, or PyPy 5.4+
* Windows, Linux, or MacOS.
* Linux requires the libsdl2 package and must be installed from source.

Extra requirements when installing directly from source
-------------------------------------------------------

* MinGW_ must be on the Windows path for use with pycparser.
  An equivalent C parser (such as `gcc`) must be installed on other OS's.
* Linux requires the packages:
  `gcc` `libsdl2-dev` `libffi-dev` `python-dev` `libomp-dev`
* SDL2 is installed automatically on Windows and MacOS

=========
 License
=========
libtcod-cffi is distributed under the Simplified 2-clause FreeBSD license.
Read LICENSE.txt_ for more details.

.. _LICENSE.txt: https://github.com/HexDecimal/libtcod-cffi/blob/master/LICENSE.txt

.. _python-tdl: https://github.com/HexDecimal/python-tdl/

.. _cffi: https://cffi.readthedocs.io/en/latest/

.. _numpy: https://docs.scipy.org/doc/numpy/user/index.html

.. _libtcod: https://bitbucket.org/libtcod/libtcod/

.. _pip: https://pip.pypa.io/en/stable/installing/

.. _MinGW: http://www.mingw.org/

.. _homebrew: http://brew.sh/

.. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/7c6bj01971ic3omd/branch/master?svg=true
    :target: https://ci.appveyor.com/project/HexDecimal/libtcod-cffi/branch/master

.. |Travis| image:: https://travis-ci.org/HexDecimal/libtcod-cffi.svg?branch=master
    :target: https://travis-ci.org/HexDecimal/libtcod-cffi

.. |Coveralls| image:: https://coveralls.io/repos/github/HexDecimal/libtcod-cffi/badge.svg?branch=master
    :target: https://coveralls.io/github/HexDecimal/libtcod-cffi?branch=master

.. |Codecov| image:: https://codecov.io/gh/HexDecimal/libtcod-cffi/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/HexDecimal/libtcod-cffi

.. |PyPI| image:: https://img.shields.io/pypi/v/libtcod-cffi.svg?maxAge=10800
    :target: https://pypi.python.org/pypi/libtcod-cffi

.. |LicenseBadge| image:: https://img.shields.io/pypi/l/libtcod-cffi.svg?maxAge=2592000
    :target: https://github.com/HexDecimal/libtcod-cffi/blob/master/LICENSE.txt

.. |ImplementationBadge| image:: https://img.shields.io/pypi/implementation/libtcod-cffi.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/libtcod-cffi

.. |VersionsBadge| image:: https://img.shields.io/pypi/pyversions/libtcod-cffi.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/libtcod-cffi

.. |Issues| image:: https://img.shields.io/github/issues/HexDecimal/libtcod-cffi.svg?maxAge=3600
    :target: https://github.com/HexDecimal/libtcod-cffi/issues

.. |Codacy| image:: https://img.shields.io/codacy/grade/4e6b8926dbb04ae183e7f62b1d842caf.svg?maxAge=10800
    :target: https://www.codacy.com/app/4b796c65-github/libtcod-cffi

.. |RTD| image:: https://readthedocs.org/projects/libtcod-cffi/badge/?version=latest
    :target: http://libtcod-cffi.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Scrutinizer| image:: https://scrutinizer-ci.com/g/HexDecimal/libtcod-cffi/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/HexDecimal/libtcod-cffi/

.. |Requires| image:: https://requires.io/github/HexDecimal/libtcod-cffi/requirements.svg?branch=master
    :target: https://requires.io/github/HexDecimal/libtcod-cffi/requirements/?branch=master
    :alt: Requirements Status

.. |Pyup| image:: https://pyup.io/repos/github/hexdecimal/libtcod-cffi/shield.svg
     :target: https://pyup.io/repos/github/hexdecimal/libtcod-cffi/
