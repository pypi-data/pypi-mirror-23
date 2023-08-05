========
Overview
========



Check if a package name is registered with PyPI

* Free software: MIT license

Installation
============

::

    pip install check-pypi-name

Documentation
=============

https://python-check-pypi-name.readthedocs.io/

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

0.3.0 (2017-06-24)
------------------

* Cleanup and Improvements

0.2.0 (2017-06-24)
------------------

* Cleanup and Improvements

0.1.0 (2017-06-23)
------------------

* First release on PyPI.


