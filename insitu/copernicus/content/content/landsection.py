""" InSitu content-types
"""
from zope.interface import implements
from Products.ATContentTypes.content.folder import ATFolder
from insitu.copernicus.content.content.interfaces import ILandSection
from insitu.copernicus.content.content import schema


class LandSection(ATFolder):
    """ Section
    """
    implements(ILandSection)

    meta_type = 'LandSection'
    portal_type = 'LandSection'
    archetype_name = 'LandSection'
    schema = schema.SECTION_SCHEMA
