========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
        | |landscape|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/ty/badge/?style=flat
    :target: https://readthedocs.org/projects/ty
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ngoldbaum/ty.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ngoldbaum/ty

.. |landscape| image:: https://landscape.io/github/ngoldbaum/ty/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ngoldbaum/ty/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/ty.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ty

.. |commits-since| image:: https://img.shields.io/github/commits-since/ngoldbaum/ty/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/ngoldbaum/ty/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/ty.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/ty

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ty.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ty

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ty.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ty


.. end-badges

A mysterious package

* Free software: BSD license

Installation
============

::

    pip install ty

Documentation
=============

https://ty.readthedocs.io/

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
