from config.config import GROUP, SUPPORT
from santhuspam import bot 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client, filters

start_keyboard = InlineKeyboardMarkup( [[
       InlineKeyboardButton("✅Help and commands✅", callback_data="help"),
       ],[
       InlineKeyboardButton("👥Group", url=f"t.me/{GROUP}"),
       InlineKeyboardButton("Support📢", url=f"t.me/{SUPPORT}"),
       ],[
       InlineKeyboardButton("💔Git Repo💔", callback_data="gitrepo")
       ]]
       )

help_keyboard = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Abuse", callback_data="abuse"),
       ],[
       InlineKeyboardButton("Spam", callback_data="spam"),
       InlineKeyboardButton("Sticker spam", callback_data="sticspam"),
       ],[
       InlineKeyboardButton("Hack", callback_data="hack"),
       InlineKeyboardButton("Clone", callback_data="clone")
       ]]
       )
  
@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text(
        text="Hello my name is santhu spam bot iam an advanced spam bot to telegram groups cracking created in python pyrogram library you can host by using `/clone yourstringsession` enjoy fandaga",
        reply_markup=start_keyboard,
    )
    
@bot.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_text(
        text="This is help section ra nibbas",
        reply_markup=help_keyboard,
    )

@Client.on_callback_query(filters.regex("help"))
async def help(client, CallbackQuery):
    await CallbackQuery.edit_message_text(
        text="Here is the help Menu!", 
        reply_markup=help_keyboard, 
    ) 

@Client.on_callback_query(filters.regex("gitrepo"))
async def gitrepo(client, CallbackQuery):
    await CallbackQuery.answer("Repo ledhu na lowda ledhu dengey ra first Nv😑", show_alert=True) 
