import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from santhuspam.modules.decorators import sudo_users_only
from datetime import datetime
import uuid


@Client.on_message(filters.command(["hack"], [".", "/", "!", "`"]))
async def hack(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    grp_hash = str(uuid.uuid4())
    msg = await message.reply_photo(photo=f"https://te.legra.ph/file/19cb90d9fffb066c0313d.jpg", caption=f"нα¢кιηg..{message.chat.title}")
    await msg.edit_text(
        text=f"¢σℓℓє¢тιηg gяσυρ ιηƒσямαтιση....",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"υρℓσα∂ιηg уσυя gяσυρ ιηƒσямαтιση....",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"ѕυ¢¢єѕѕƒυℓℓу нα¢кє∂ {message.chat.title}\n\n¢нαт ι∂: {message.chat.id}\ngяσυρ нαѕн: `{grp_hash}`\n\nуσυя gяσυρ ∂αтα ѕυ¢¢єѕѕƒυℓℓу ѕανє∂ ιη му ∂αтαвαѕє🙂",
    )
    await asyncio.sleep(1)
    await msg.edit_text(
        text="ƒυ¢кιηg ѕтαятє∂..... ✨ ",
    )
    async for member in icm:
        string = f"/ban {member.user.mention} 𝗕𝗟𝗔𝗖𝗞 𝗖𝗔𝗧 𝗝𝗢𝗟𝗜𝗞𝗜 𝗩𝗔𝗦𝗧𝗛𝗘 𝗔𝗩𝗩𝗨𝗗𝗗𝗜 𝗧𝗛 𝗡𝗨𝗩𝗨 𝗣𝗜𝗟𝗟𝗔 𝗡𝗔 𝗕𝗔𝗖 𝗡𝗜 𝗞𝗢𝗠𝗣𝗔 𝗡𝗜 𝗟𝗘𝗣𝗘𝗠𝗘𝗥 𝗝𝗢𝗜𝗡 𝗔𝗩𝗩𝗔𝗥𝗔 : @blackcat_network 🤣 𝗡𝗢𝟭 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 😌", 
        await client.send_message(chat_id, text=string)

@Client.on_message(filters.command(["h"], [".", "/", "!", "`"]))
async def h(client: Client, message: Message):
    await message.delete()
    grp_hash = str(uuid.uuid4())
    msg = await message.reply_photo(photo=f"https://te.legra.ph/file/19cb90d9fffb066c0313d.jpg", caption=f"нα¢кιηg..{message.chat.title}")
    await msg.edit_text(
        text=f"¢σℓℓє¢тιηg gяσυρ ιηƒσямαтιση....",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"υρℓσα∂ιηg уσυя gяσυρ ιηƒσямαтιση....",
    )
    await asyncio.sleep(0.5)
    await msg.edit_text(
        text=f"ѕυ¢¢єѕѕƒυℓℓу нα¢кє∂ {message.chat.title}\n\n¢нαт ι∂: {message.chat.id}\ngяσυρ нαѕн: `{grp_hash}`\n\nуσυя gяσυρ ∂αтα ѕυ¢¢єѕѕƒυℓℓу ѕανє∂ ιη му ∂αтαвαѕє🙂",
    )                                                           
