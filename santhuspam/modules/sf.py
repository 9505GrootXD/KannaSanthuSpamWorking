import asyncio

from pyrogram import filters, Client 
from pyrogram.raw import functions
from pyrogram.types import Message

@Client.on_message(filters.command(["screenshot", "ss"], ".") & filters.private & filters.me)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send(
            functions.messages.SendScreenshotNotification(
                peer=await client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=client.rnd_id(),
            )
        ),
    )



