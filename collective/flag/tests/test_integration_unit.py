"""This is an integration "unit" test. It uses PloneTestCase, but does not
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
        # We need to check whether the 'flaggedobject' index has been added to the catalog
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.failUnless('flaggedobject' in catalog.indexes())

    def test_field_available(self):
        # Test that we have a field on objects
        new_id = self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        self.failUnless(new_obj.Schema().has_key('flaggedobject'))
        
    def test_field_stored(self):
        # Whether we can change the field and the value of it is getting stored
        new_id = self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        field = new_obj.Schema().getField('flaggedobject')
        field.set(new_obj, True)
        self.failUnless(field.get(new_obj))

    def test_value_stored_in_catalog(self):
        new_id = self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        
        field = new_obj.Schema().getField('flaggedobject')        
        field.set(new_obj, True)
        
        self.setRoles(('Manager',))
        new_obj.reindexObject()
        catalog = getToolByName(self.portal, 'portal_catalog')
        results = catalog.searchResults(flaggedobject = True)
        
        self.failUnless(len(results) == 1)
        self.failUnless(results[0].id == 'my-page')
    
    # Keep adding methods here, or break it into multiple classes or
    # multiple files as appropriate. Having tests in multiple files makes
    # it possible to run tests from just one package:
    #
    #   ./bin/instance test -s example.tests -t test_integration_unit


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFlags))
    return suite