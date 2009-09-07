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
        
    def test_field_available(self):
        # Test that we have a field on objects
        new_id = self.folder.invokeFactory('Document', 'my-page')
        new_obj = getattr(self.folder, 'my-page')
        self.failUnless(new_obj.Schema().has_key('flaggedobject'))    
    
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