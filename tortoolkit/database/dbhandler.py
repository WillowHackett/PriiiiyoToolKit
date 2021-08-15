from ..config.ExecVarsSample import ExecVars
import os

dburl = os.environ.get("DATABASE_URL",None)
if dburl is None:
    dburl = ExecVars.DATABASE_URL

from .upload_db import TtkUpload

if "mongo" in dburl:
    from .mongo_impl import TorToolkitDB, UserDB, TtkTorrents
else:
    from .postgres_impl import TorToolkitDB, UserDB, TtkTorrents
