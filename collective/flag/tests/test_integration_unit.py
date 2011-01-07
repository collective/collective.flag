"""This is an integration test. It uses PloneTestCase, but does not
use doctest syntax.

You will find lots of examples of this type of test in CMFPlone/tests, for
example.
"""

import unittest
from collective.flag.tests.base import FlagTestCase

from Products.CMFCore.utils import getToolByName


class TestFlags(FlagTestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_able_to_add_document(self):
        new_id = self.folder.invokeFactory('Document', 'my-page')
        self.assertEquals('my-page', new_id)

    def test_index(self):
        # Check whether the index has been added to the catalog
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.failUnless('flaggedobject' in catalog.indexes())

    def test_field_available(self):
        # Test that we have a field on objects
        self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        self.failUnless('flaggedobject' in new_obj.Schema().keys())

    def test_field_stored(self):
        # Can we change the field? Is the value of it getting stored?
        new_obj = self.folder.invokeFactory('Document', 'my-page',
                                            flaggedobject=True)
        new_obj = getattr(self.folder, 'my-page')
        field = new_obj.Schema().getField('flaggedobject')
        self.failUnless(field.get(new_obj))

    def test_value_stored_in_catalog(self):
        self.folder.invokeFactory('Document', 'my-page', flaggedobject=True)
        catalog = getToolByName(self.portal, 'portal_catalog')
        results = catalog.searchResults(flaggedobject = True)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 'my-page')


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFlags))
    return suite
