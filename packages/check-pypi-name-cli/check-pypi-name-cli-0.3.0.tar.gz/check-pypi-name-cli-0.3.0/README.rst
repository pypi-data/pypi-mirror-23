========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape| |scrutinizer| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-check-pypi-name-cli/badge/?style=flat
    :target: https://readthedocs.org/projects/python-check-pypi-name-cli
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-check-pypi-name-cli.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-check-pypi-name-cli

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-check-pypi-name-cli?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-check-pypi-name-cli

.. |requires| image:: https://requires.io/github/techdragon/python-check-pypi-name-cli/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-check-pypi-name-cli/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/techdragon/python-check-pypi-name-cli/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-check-pypi-name-cli

.. |landscape| image:: https://landscape.io/github/techdragon/python-check-pypi-name-cli/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/python-check-pypi-name-cli/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/python-check-pypi-name-cli/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/python-check-pypi-name-cli
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/check-pypi-name-cli.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/check-pypi-name-cli

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-check-pypi-name-cli/v0.3.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-check-pypi-name-cli/compare/v0.3.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/check-pypi-name-cli.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/check-pypi-name-cli

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/check-pypi-name-cli.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/check-pypi-name-cli

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/check-pypi-name-cli.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/check-pypi-name-cli

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/techdragon/python-check-pypi-name-cli/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/techdragon/python-check-pypi-name-cli/


.. end-badges

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
