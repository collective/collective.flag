Introduction
============

**collectiv.flag** is a simple package that adds an option of marking special objects in a Plone site - flagging them. By simple additional field added to ``Settings`` schemata one can differentiate regular documents from the special ones. Possible usecases:
    * put items to the frontpage. Usually not every most recent item should go to the frontpage, but those having a special meaning;
    * be able to search for items that are special when building a Collection.

Tips
====

Re-name the field's title
*************************
There is not easy way of renaming field's title using a controlpanel or
something like that. What you can do instead - translate the title using
standard mechanizms of Plone.

General solutions - override translation for ``label_flaggedobject_title``
msgid from **collective.flag** domain. Read more about how to do this in Plone
v. > 3.0 here - `i18n, locales and Plone 3.0
<http://maurits.vanrees.org/weblog/archive/2007/09/i18n-locales-and-plone-3.0>`_.


