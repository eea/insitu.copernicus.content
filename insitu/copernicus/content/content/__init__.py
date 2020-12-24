""" Custom content
"""
from Products.ATContentTypes.content.base import registerATCT
from insitu.copernicus.content.config import PACKAGE_NAME
from insitu.copernicus.content.content import landfile
from insitu.copernicus.content.content import landitem
from insitu.copernicus.content.content import landsection


def register():
    """ Register custom content-types
    """
    registerATCT(landsection.LandSection, PACKAGE_NAME)
    registerATCT(landitem.LandItem, PACKAGE_NAME)
    registerATCT(landfile.LandFile, PACKAGE_NAME)
