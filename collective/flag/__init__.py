# from Products.CMFPlone.CatalogTool import registerIndexableAttribute

from plone.indexer.decorator import indexer

from Products.ATContentTypes.interface import IATContentType

@indexer(IATContentType)
def flag_indexer(obj):
    """A method for indexing 'frontpagearticle' field of Documents
    """
    field = obj.Schema().getField('flaggedobject')
    if field is not None:
        return field.get(obj)
    else:
        raise AttributeError            

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
