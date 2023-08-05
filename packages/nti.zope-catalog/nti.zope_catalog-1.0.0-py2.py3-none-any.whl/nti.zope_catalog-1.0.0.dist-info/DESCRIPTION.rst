=================
 nti.zope_catalog
=================

.. image:: https://travis-ci.org/NextThought/nti.zope_catalog.svg?branch=master
    :target: https://travis-ci.org/NextThought/nti.zope_catalog

.. image:: https://coveralls.io/repos/github/NextThought/nti.zope_catalog/badge.svg?branch=master
    :target: https://coveralls.io/github/NextThought/nti.zope_catalog?branch=master

.. image:: https://readthedocs.org/projects/ntizope-catalog/badge/?version=latest
    :target: http://ntizope-catalog.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Utilities and extensions for ZODB-based Zope catalogs and indexes.

This builds on both zope.catalog and zc.catalog.


=========
 Changes
=========

1.0.0 (2017-06-15)
==================

- First PyPI release.
- Add support for Python 3.
- ``TimestampNormalizer`` also normalizes incoming datetime objects.
- Fix extent-based queries for NormalizedKeywordIndex.
- 100% test coverage.


