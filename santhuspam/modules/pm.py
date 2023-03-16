from pyrogram import filters, Client
import asyncio
from config.config import SUDO_USER
from pyrogram.methods import messages
from santhuspam.modules.pmguard import get_arg, denied_users
import database.pmguard as santhu




@Client.on_message(filters.command("pmguard", [".", "/", "!", "?", "%", "*",]))
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Iam now understand only on or off**")
        return
    if arg == "off":
        await santhu.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await santhu.set_pm(True)
        await message.edit("**PM Guard Activated**")
        
@Client.on_message(filters.command("setpmmsg", ["."]))
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await santhu.set_permit_message(santhu.PM_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await santhu.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")
