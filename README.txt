------------
Introduction
------------

`collective.flag` is a simple package that adds an option of marking special
objects in a Plone site - flagging them. An additional field added to the
``Settings`` schemata can be used to differentiate regular documents from the
special ones. Possible use-cases:

* Put items to the frontpage. Usually not every most recent item should go
  to the frontpage, but those having a special meaning;

* Allow to search for items that are special when building a ``Collection``.


----
Tips
----

Rename the field's title
========================

There is not easy way of renaming field's title using a controlpanel or
something like that. What you can do instead - translate the title using
standard mechanisms of Plone.

The recommended solution is to override the translation for the
``label_flaggedobject_title`` msgid in the ``collective.flag`` domain. Read
more about how to do this in Plone 3.x or later here - `i18n, locales and
Plone 3.0`__.


Developed by **Jarn AS** — http://www.jarn.com

Development sponsored by the **Bergen Public Library** - http://www.nettbiblioteket.no

  .. __: http://maurits.vanrees.org/weblog/archive/2007/09/i18n-locales-and-plone-3.0
  