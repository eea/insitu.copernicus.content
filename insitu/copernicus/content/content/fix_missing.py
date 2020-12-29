from persistent import Persistent
from plone.app.upgrade.utils import alias_module


class UserDataSchemaProvider(Persistent):
    def wl_isLocked(self):
        return False

alias_module(
    'land.copernicus.content.userdataschema',
    UserDataSchemaProvider
)
