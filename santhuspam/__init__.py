import logging
from pyrogram import Client, filters
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config.config import *
from typing import Tuple
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

clients = []
ids = []

API_ID = API_ID
API_HASH = API_HASH 
STRING_SESSION = STRING_SESSION
BOT_TOKEN = BOT_TOKEN

if not STRING_SESSION:
    logging.error("Authorized STRING SESSION error")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1) 
    
if not BOT_TOKEN:
    logging.error("No bot token founded exiting from terminal")
    quit(1) 

bot = Client(
    "santhunibba",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="santhuspam/assistant")
)

if STRING_SESSION:
   print("Client: Found.. Starting..📳")
   client = Bot(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="santhuspam.modules"))
   clients.append(client)
