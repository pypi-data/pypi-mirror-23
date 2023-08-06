Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.2.3
-----
2017-07-13

- More tests.

0.2.2
-----
2017-07-04

- Documentation improvements.
- Tested against various Django REST framework versions (>=3.5.0,<=3.6.3).

0.2.1
-----
2017-07-04

- Minor fixes.
- Documentation improvements.

0.2
---
2017-07-02

- Handle unlimited nesting depth for nested serializers of non-relational
  fields.
- Documentation improvements.

0.1.8
-----
2017-07-01

- Initial beta release.
