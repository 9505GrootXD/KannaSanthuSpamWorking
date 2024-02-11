from pyrogram import Client, filters
from config.config import API_ID, API_HASH, STRING_SESSION
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client
from config.config import MONGO_DB_URL
from santhuspam.modules.logger import LOGGER
import glob
from os.path import dirname, isfile
from pytgcalls import PyTgCalls, idle

def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]


bot = Client(
    ":spambot:",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION, 
    plugins=dict(root="santhuspam.modules")
) 
call_py = PyTgCalls(bot)



_mongo_async_ = _mongo_client_(MONGO_DB_URL)
_mongo_sync_ = MongoClient(MONGO_DB_URL)

mongodb = _mongo_async_.santhuspam
pymongodb = _mongo_sync_.santhuspam

dbb = _mongo_async_["SANTHUDB"]
