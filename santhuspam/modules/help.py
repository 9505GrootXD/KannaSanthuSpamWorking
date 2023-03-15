from pyrogram import Client, filters
from pyrogram.types import Message
from santhuspam.modules.decorators import sudo_users_only


@Client.on_message(filters.command(["help"], [".", "/", "!", "`"]))
@sudo_users_only
async def help(client: Client, message: Message): 
    await message.reply_text(
        text=f"""here is the Help Menu!\n\n𝗧𝗵𝗶𝘀 𝗶𝘀 𝗺𝘆 𝘂𝘀𝗲𝗿 𝗯𝗼𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀:
𝗕𝗼𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀:
✘ .porn 3 porn spam to users or grps. 
✘ .sexstick 2 this is sex stickers spam. 
✘ .abuse 3 to abuse users. 
✘ .hack just hack with banall in grps. 
✘ .h normal prank hack with userbot. 
✘ .stick spam normal stickers. 
✘ .help see 👀 help what do you need specific commands. 

©copyright infringement on Blackcat Network: @BlackCatFighters
Owner: @blackcatxowner

Note: host your bot using this bot @Veezmegaguardbot  just type /clone yourstringsession""",
   ) 
