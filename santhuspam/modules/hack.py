import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from santhuspam.decorators import sudo_users_only
from datetime import datetime

@Client.on_message(filters.command(["hack"], [".", "/", "!", "`"]))
@sudo_users_only
async def banall(client: Client, message: Message):
    msg = await message.reply_photo(photo=f"https://te.legra.ph/file/19cb90d9fffb066c0313d.jpg", caption=f"нα¢кιηg..{message.chat.title}")
    await asyncio.sleep(0.3) 
    await msg.edit_text(
        text=f"ѕυ¢¢єѕѕƒυℓℓу нα¢кє∂ {message.chat.title}\n\n¢нαт ι∂: {message.chat.id}\n\nуσυя gяσυρ ∂αтα ѕυ¢¢єѕѕƒυℓℓу ѕανє∂ ιη му ∂αтα вαѕє🙂",
    ) 
