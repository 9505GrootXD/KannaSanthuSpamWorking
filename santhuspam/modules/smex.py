import asyncio
import random
import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import PORN 
from traceback import format_exc
from typing import Tuple
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from spam.decorators import sudo_users_only


@Client.on_message(filters.command(["porn", "hibro"], [".", "!", "/", "'"]))
@sudo_users_only
async def porn(client: Client, message: Message):       
    sex = await message.reply_text("**Processing.. Your hmm 😁**")
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    for _ in range(quantity):
        try: 
            file = random.choice(PORN) 
            await client.send_video(chat_id=message.chat.id, video=file)       
        except FloodWait as e:
            await asyncio.sleep(e.x)
