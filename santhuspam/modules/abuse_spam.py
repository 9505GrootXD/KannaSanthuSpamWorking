#telugu coders

import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config.config import ABUSE_SPAM
from typing import Tuple
import random
import asyncio
from traceback import format_exc
from pyrogram.errors import FloodWait
from santhuspam.modules.decorators import sudo_users_only

@Client.on_message(filters.command(["abuse"], [".", "!", "/", "`"]))
async def spam(client: Client, message: Message):   
    await message.delete() 
    spam = await message.reply_text("**Process your abuse spam....**")
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    for _ in range(quantity):
        try: 
            text = random.choice(ABUSE_SPAM) 
            await client.send_message(chat_id=message.chat.id, text=text)       
        except FloodWait as e:
            await asyncio.sleep(e)
