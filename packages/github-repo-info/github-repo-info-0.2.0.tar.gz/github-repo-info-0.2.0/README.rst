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
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-github-repo-info/badge/?style=flat
    :target: https://readthedocs.org/projects/python-github-repo-info
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-github-repo-info.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-github-repo-info

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-github-repo-info?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-github-repo-info

.. |requires| image:: https://requires.io/github/techdragon/python-github-repo-info/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-github-repo-info/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/techdragon/python-github-repo-info/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/techdragon/python-github-repo-info

.. |codecov| image:: https://codecov.io/github/techdragon/python-github-repo-info/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-github-repo-info

.. |landscape| image:: https://landscape.io/github/techdragon/python-github-repo-info/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/python-github-repo-info/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/python-github-repo-info/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/python-github-repo-info
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/github-repo-info.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/github-repo-info

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-github-repo-info/v0.2.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-github-repo-info/compare/v0.2.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/github-repo-info.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/github-repo-info

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/github-repo-info.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/github-repo-info

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/github-repo-info.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/github-repo-info

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/techdragon/python-github-repo-info/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/techdragon/python-github-repo-info/


.. end-badges

Provides access to a local GitHub repository's configuration.

* Free software: MIT license

Installation
============

::

    pip install github-repo-info

Documentation
=============

https://python-github-repo-info.readthedocs.io/

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
