========
Overview
========



nextstep-plist is a python 3 compatible fork of the nsplist package
that provides a parser for the NeXTSTEP plist text-based format.
A common usage is parsing iTunes In App Purchase receipts to be
able to reject them early, without having to make a
request to the iTunes API.

This is distinct from the Apple plist format, which has more
supported types and serialises to XML or binary.

* Free software: MIT license

Installation
============

::

    pip install nextstep-plist

Documentation
=============

https://python-nextstep-plist.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


Changelog
=========

0.1.0 (2017-06-25)
------------------

* First release on PyPI.


