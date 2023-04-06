import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from santhuspam.modules.decorators import sudo_users_only
from datetime import datetime


@Client.on_message(filters.command(["hack"], [".", "/", "!", "`"]))
async def hack(client: Client, message: Message):
    await message.delete()
    userid = m.from_user.mention
    msg = await message.reply_text(text="𝗕𝗼𝘁𝘁𝘁𝗶𝗻𝗴 𝗺𝘆 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲....🔥")
    await msg.edit_text(
        text=f"𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗻𝗴 𝘁𝗵𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻..🧐🧐🧐",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝘀𝗼𝗺𝗲 𝗯𝗶𝘁𝗰𝗵𝘀 𝗶𝗻 𝗺𝘆 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲....😉",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"**𝗧𝗮𝗿𝗴𝗲𝘁 {m.from_user.mention()} 𝗱𝗲𝗮𝘁𝗹𝗶𝘀 𝘀𝗮𝘃𝗲𝗱 𝗼𝗻 𝗺𝘆 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝘁𝗼 𝗿𝗲𝗺𝗼𝘃𝗲 𝗽𝗮𝘆 𝟭𝟬$ 𝗧𝗼 `kannaxd@ybl`....**",
    )
    

@Client.on_message(filters.command(["kanna"], [".", "/", "!", "`"]))
async def kanna(client: Client, message: Message):
    await message.delete()
    msg = await message.reply_text("𝗸𝗮𝗻𝗻𝗮𝘅𝗗")
    await msg.edit_text(
        text=f"𝗺𝗲𝗵𝗮𝗯𝗼𝗼𝗯𝗮 𝗺𝗲𝗵𝗮𝗯𝗼𝗼𝗯𝗮 💫🥂",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"𝗺𝗮𝘆 𝘁𝗲𝗿𝗶 𝗺𝗲𝗵𝗮𝗯𝗼𝗼𝗯𝗮 😉😍",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"𝗺𝗲𝗵𝗮𝗯𝗼𝗼𝗯𝗮 𝗹𝗲𝗱𝗵𝘂 𝗺𝗼𝗱𝗱𝗮 𝗹𝗲𝗱𝗵𝘂 𝗱𝗲𝗻𝗴𝗲𝘆😄",
    )                                                           
