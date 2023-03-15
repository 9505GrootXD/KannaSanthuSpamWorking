import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from santhuspam.modules.decorators import sudo_users_only

@Client.on_message(filters.command(["banall"], [".", "/", "!", "`"]))
@sudo_users_only
async def banall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n𝗯𝗮𝗻𝗻𝗲𝗱 𝗯𝘆 🥀👅[𝗯𝗹𝗮𝗰𝗸𝗰𝗮𝘁](https://t.me/BlackcatXofficial).🐈‍⬛"
        await client.send_message(chat_id, text=string)
