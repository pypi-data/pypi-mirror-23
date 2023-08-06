``zope.schema``
===============

.. image:: https://img.shields.io/pypi/v/zope.schema.svg
    :target: https://pypi.python.org/pypi/zope.schema/
    :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.schema.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.schema

.. image:: https://readthedocs.org/projects/zopeschema/badge/?version=latest
        :target: http://zopeschema.readthedocs.org/en/latest/
        :alt: Documentation Status

Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods).  Every schema is an interface and
specifies the public fields of an object.  A *field* roughly
corresponds to an attribute of a Python object.  But a Field provides
space for at least a title and a description.  It can also constrain
its value and provide a validation method.  Besides you can optionally
specify characteristics such as its value being read-only or not
required.

See https://zopeschema.readthedocs.io/ for more information.
