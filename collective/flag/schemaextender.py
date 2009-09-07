from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.markerfield.field import InterfaceMarkerField

from Products.ATContentTypes.interface import IATContentType
from Products.Archetypes.atapi import BooleanWidget

# from Products.ATContentTypes.interface.document import IATDocument

from collective.flag.interfaces import IFlaggableObject

_ = MessageFactory('collective.flag')

class ContentTypeExtender(object):
    """Adapter that adds custom metadata."""
    adapts(IATContentType)

    implements(ISchemaExtender)

    _fields = [
        InterfaceMarkerField("flaggedobject",
            schemata = "settings",
            interfaces = (IFlaggableObject,),
            languageIndependent = True,
            widget = BooleanWidget(
                label = _(u"label_flaggedobject_title",
                    default=u"Mark this object as important."),
                description = _(u"help_flaggedobject",
                    default=u""),
                ),
            ),
        ]
    
    def __init__(self, contentType):
        pass

    def getFields(self):
        return self._fields
