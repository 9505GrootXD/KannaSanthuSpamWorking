import asyncio
import random
import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config.config import PORN_STICK_SPAM, STICKER_SPAM
from traceback import format_exc
from typing import Tuple
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from santhuspam.modules.decorators import sudo_users_only


@Client.on_message(filters.command(["stick"], [".", "!", "/", "'"]))
@sudo_users_only
async def stick(client: Client, message: Message):       
    sticker = await message.reply_text("**Processing your sticker spam...**")
    await message.delete() 
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    for _ in range(quantity):
        try: 
            stick = random.choice(STICKER_SPAM) 
            await client.send_sticker(chat_id=message.chat.id, sticker=stick)       
        except FloodWait as e:
            await asyncio.sleep(e.x)


@Client.on_message(filters.command(["sexstick"], [".", "!", "/", "'"]))
@sudo_users_only
async def sexstick(client: Client, message: Message):       
    sticker = await message.reply_text("**Processing your sex sticker spam...**")
    await message.delete() 
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    for _ in range(quantity):
        try: 
            stick = random.choice(PORN_STICK_SPAM) 
            await client.send_sticker(chat_id=message.chat.id, sticker=stick)       
        except FloodWait as e:
            await asyncio.sleep(e.x)
