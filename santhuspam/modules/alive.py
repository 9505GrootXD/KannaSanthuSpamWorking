import sys
import datetime

from os import execle, environ
from config.config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


KANNA = f"""❖ 𝗔𝗺𝗮𝗹𝗮𝗫𝘂𝘀𝗲𝗿𝗕𝗼𝘁 ❖
➻ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.11.1`
➻ **ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ** : `1.4.16`
➻ **xꜱᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `3.3`
➻ **ᴜᴘᴅᴀᴛᴇꜱ** : [ᴀᴍᴀʟᴀsᴜᴘᴘᴏʀᴛ](https://t.me/tgshadow_fighters)\n"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"➻ ᴛʜᴇ ᴀᴍᴀʟᴀ\n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `3.3`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(kanna: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await kanna.send_photo(msg.chat.id, ALIVE_PIC, caption=KANNA)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await kanna.send_video(msg.chat.id, ALIVE_PIC, caption=KANNA)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
