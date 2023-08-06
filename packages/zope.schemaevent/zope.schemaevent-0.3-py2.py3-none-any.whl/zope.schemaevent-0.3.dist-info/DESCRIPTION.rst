.. contents::

Introduction
============

Enable handler for event triggered on field by adding subscriber.
We make the configuration glue between `zope.schema` (which doesn't depend on zope.component) and `zope.component`.

Example::

    <subscriber
       for=".interfaces.IExampleObject
            zope.schema.interfaces.IText
            zope.schema.interfaces.IFieldUpdatedEvent"
       handler=".localrolefield.set_local_role_on_object" />


Contributors
============

- Affinitic, Bubblenet - Original Author
- IMIO - Client

Changelog
=========

0.3 (2017-07-13)
----------------

- Add support for Python 3.4, 3.5, 3.6 and PyPy.

- Drop support for Python 2.6.

0.2 (2014-01-30)
----------------

- Fix release, better manifest.in
  [jfroche]


0.1 (2014-01-22)
----------------

- Initial release
  [jfroche]

- Package created using templer
  [jfroche]



