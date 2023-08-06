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

.. |docs| image:: https://readthedocs.org/projects/python-git-repo-info/badge/?style=flat
    :target: https://readthedocs.org/projects/python-git-repo-info
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-git-repo-info.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-git-repo-info

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-git-repo-info?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-git-repo-info

.. |requires| image:: https://requires.io/github/techdragon/python-git-repo-info/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-git-repo-info/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/techdragon/python-git-repo-info/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/techdragon/python-git-repo-info

.. |codecov| image:: https://codecov.io/github/techdragon/python-git-repo-info/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-git-repo-info

.. |landscape| image:: https://landscape.io/github/techdragon/python-git-repo-info/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/python-git-repo-info/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/python-git-repo-info/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/python-git-repo-info
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/git-repo-info.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/git-repo-info

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-git-repo-info/v0.4.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-git-repo-info/compare/v0.4.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/git-repo-info.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/git-repo-info

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/git-repo-info.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/git-repo-info

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/git-repo-info.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/git-repo-info

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/techdragon/python-git-repo-info/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/techdragon/python-git-repo-info/


.. end-badges

Provides access to a local git repository's configuration.

* Free software: MIT license

Installation
============

::

    pip install git-repo-info

Documentation
=============

https://python-git-repo-info.readthedocs.io/

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
