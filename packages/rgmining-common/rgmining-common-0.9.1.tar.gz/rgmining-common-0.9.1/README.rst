Common library for Review Graph Mining
======================================

|GPLv3| |Build Status| |wercker status| |Code Climate| |Release|

The common module and its submodules probides varies functions ans
classes which can be used in any context.

The main functions provided by this package are followings:

-  ``print_args``: Decorate a function so that print arguments before
   calling it.
-  ``print_return``: Decorate a function so that print result after
   calling it.
-  ``constant``: Decorate a function so that the result is a constant
   value.
-  ``memoized``: Decorate a function to memoize results.

See `documents <https://rgmining.github.io/common/>`__ for more
information.

Installation
------------

Use ``pip`` to install this package.

::

    pip install --upgrade rgmining-common

License
-------

This software is released under The GNU General Public License Version
3, see `COPYING <COPYING>`__ for more detail.

.. |GPLv3| image:: https://img.shields.io/badge/license-GPLv3-blue.svg
   :target: https://www.gnu.org/copyleft/gpl.html
.. |Build Status| image:: https://travis-ci.org/rgmining/common.svg?branch=master
   :target: https://travis-ci.org/rgmining/common
.. |wercker status| image:: https://app.wercker.com/status/00645c6dedb906005bbc6c080290f5f6/s/master
   :target: https://app.wercker.com/project/byKey/00645c6dedb906005bbc6c080290f5f6
.. |Code Climate| image:: https://codeclimate.com/github/rgmining/common/badges/gpa.svg
   :target: https://codeclimate.com/github/rgmining/common
.. |Release| image:: https://img.shields.io/badge/release-0.9.1-brightgreen.svg
   :target: https://github.com/rgmining/common/releases/tag/v0.9.1
