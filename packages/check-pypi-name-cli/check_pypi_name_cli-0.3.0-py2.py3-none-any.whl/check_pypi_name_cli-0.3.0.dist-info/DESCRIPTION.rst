========
Overview
========



A command line tool that checks if a package name is reserved or in use on PyPI.

* Free software: BSD license

Installation
============

::

    pip install check-pypi-name-cli

Documentation
=============

https://python-check-pypi-name-cli.readthedocs.io/

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


