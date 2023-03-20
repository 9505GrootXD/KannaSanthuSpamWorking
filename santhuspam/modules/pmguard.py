from pyrogram import filters, Client
import asyncio
from pyrogram.types import Message 
from pyrogram.methods import messages
from database.pm import get_approved_users, pm_guard
import database.pm as santhu
from config.config import LOG_GROUP, PM_LOGGER

FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.command("setlimit", [".", "!", "/"]))
async def setlimit(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await santhu.set_limit(int(arg))
    await message.edit(f"**Limit set to {arg}**")



@Client.on_message(filters.command("setblockmsg", [".", "/"]))
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await santhu.set_block_message(santhu.BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await santhu.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")


@Client.on_message(filters.command(["approve"], [".", "/"]) & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await santhu.get_pm_settings()
    await santhu.allow_user(chat_id)
    await message.edit(f"**I have allowed [you](tg://user?id={chat_id}) to PM me.**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["disapprove"], [".", "/"]) & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await santhu.deny_user(chat_id)
    await message.edit(f"**I have denied [you](tg://user?id={chat_id}) to PM me.**")
