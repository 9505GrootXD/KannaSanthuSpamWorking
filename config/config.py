import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "9276915")) 
API_HASH = getenv("API_HASH", "e8145ec48504292485900892fffaf890") 
BOT_TOKEN = getenv("BOT_TOKEN", "5842233190:AAF8F4za-ClANrHxsNlSeIf78vNZ7rl7v_o")
STRING_SESSION = getenv("STRING_SESSION", "BQDEbNWHw-45n14dG3WrkedmRi75z0FiF9YQcjel39bjNMkwjmGWWgw3mTEc5Gq-FBA4CHBSrLOfzPCz8AafWzCG_OnZifjm6ZMQvohFw9eZgABZ3BqSVS1joJ4hrjXkb8JVRHR0hP1fm3qB9tr6FuxKXNKjsiGDHNczRjC4txFOam9l8qbUrHRLpxnQXPstl0cqH1e5jFWSx4oNKOuVL-x25CqB-g-Cfom8fCaGK2FZSERLxPfYoKjNLMx0a8QIv8F1APL9eZCnUhJPux1omAYgDpSdRgDfBXrCMQryAlTfF-ewJZlIU8Yi2HkBq89SLxhaG26kdwR7fzxkrENVp4EcAAAAAUvMGDwA") 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5566634044").split()))
OWNER_ID  = getenv("OWNER_ID", "5566634044")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Amala203145:Amala2031456@cluster0.t9ibfge.mongodb.net/?retryWrites=true&w=majority")
GROUP  = getenv("GROUP", "BlackCatFighters")
SUPPORT  = getenv("SUPPORT", "BlackCatFighters")


PORN = [
        "https://telegra.ph/file/9bcc076fd81dfe3feb291.mp4",
        "https://telegra.ph/file/b7a1a42429a65f64e67af.mp4",
        "https://telegra.ph/file/dc3da5a3eb77ae20fa21d.mp4",
        "https://telegra.ph/file/7b15fbca08ae1e73e559c.mp4",
        "https://telegra.ph/file/a9c1dea3f34925bb60686.mp4",
        "https://telegra.ph/file/913b4e567b7f435b7f0db.mp4",
        "https://telegra.ph/file/5a5d1a919a97af2314955.mp4",
        "https://telegra.ph/file/0f8b903669600d304cbe4.mp4",
        "https://telegra.ph/file/f3816b54c9eb7617356b6.mp4",
        "https://telegra.ph/file/516dbaa03fde1aaa70633.mp4",
        "https://telegra.ph/file/07bba6ead0f1e381b1bd1.mp4",
        "https://telegra.ph/file/0a4f7935df9b4ab8d62ed.mp4",
        "https://telegra.ph/file/40966bf68c0e4dbe18058.mp4",
        "https://telegra.ph/file/50637aa9c04d136687523.mp4",
        "https://telegra.ph/file/b81c0b0e491da73e64260.mp4",
        "https://telegra.ph/file/4ddf5f29783d92ae03804.mp4",
        "https://telegra.ph/file/4037dc2517b702cc208b1.mp4",
        "https://telegra.ph/file/33cebe2798c15d52a2547.mp4",
        "https://telegra.ph/file/4dc3c8b03616da516104a.mp4",
        "https://telegra.ph/file/6b148dace4d987fae8f3e.mp4",
        "https://telegra.ph/file/8cb081db4eeed88767635.mp4",
        "https://telegra.ph/file/98d3eb94e6f00ed56ef91.mp4",
        "https://telegra.ph/file/1fb387cf99e057b62d75d.mp4",
        "https://telegra.ph/file/6e1161f63879c07a1f213.mp4",
        "https://telegra.ph/file/0bf4defb9540d2fa6d277.mp4",
        "https://telegra.ph/file/d5f8280754d9aa5dffa6a.mp4",
        "https://telegra.ph/file/0f23807ed1930704e2bef.jpg",
        "https://telegra.ph/file/c49280b8f1dcecaf86c00.jpg",
        "https://telegra.ph/file/f483400ff141de73767ca.jpg",
        "https://telegra.ph/file/1543bbea4e3c1abb6764a.jpg",
        "https://telegra.ph/file/a0d77be0d769c7cd334ab.jpg",
        "https://telegra.ph/file/6c6e93860527d2f577df8.jpg",
        "https://telegra.ph/file/d987b0e72eb3bb4801f01.jpg",
        "https://telegra.ph/file/b434999287d3580250960.jpg",
        "https://telegra.ph/file/0729cc082bf97347988f7.jpg",
        "https://telegra.ph/file/bb96d25df82178a2892e7.jpg",
        "https://telegra.ph/file/be73515791ea33be92a7d.jpg",
        "https://telegra.ph/file/fe234d6273093282d2dcc.jpg",
        "https://telegra.ph/file/66254bb72aa8094d38250.jpg",
        "https://telegra.ph/file/44bdaf37e5f7bdfc53ac6.jpg",
        "https://telegra.ph/file/e561ee1e1ca88db7e8038.jpg",
        "https://telegra.ph/file/f1960ccfc866b29ea5ad2.jpg",
        "https://telegra.ph/file/97622cad291472fb3c4aa.jpg",
        "https://telegra.ph/file/a46e316b413e9dc43e91b.jpg",
        "https://telegra.ph/file/497580fc3bddc21e0e162.jpg",
        "https://telegra.ph/file/3e86cc6cab06a6e2bde82.jpg",
        "https://telegra.ph/file/83140e2c57ddd95f310e6.jpg",
        "https://telegra.ph/file/2b20f8509d9437e94fed5.jpg",
        "https://telegra.ph/file/571960dcee4fce56698a4.jpg",
        "https://telegra.ph/file/25929a0b49452d8946c14.mp4",
        "https://telegra.ph/file/f5c9ceded3ee6e76a5931.jpg",
        "https://telegra.ph/file/a8bf6c6df8a48e4a306ca.jpg",
        "https://telegra.ph/file/af9e3f98da0bd937adf6e.jpg",
        "https://telegra.ph/file/2fcccbc72c57b6892d23a.jpg",
        "https://telegra.ph/file/843109296a90b8a6c5f68.jpg",
]


ABUSE_SPAM = [
    "Ni amma puka ra lanjakoda", 
    "Me amma ani red light area lo denga", 
    "Me amma gudha free ga amutha", 
    "ɢᴜᴅʜᴀ ᴍᴜsᴜᴋᴏɴɪ ᴋᴜʀᴄʜᴏ sᴜʟɪ ɢᴀ", 
    "ᴀᴛʜᴜᴋᴜ ʀᴀɴɪ ᴠᴀᴅᴜ ᴋᴏᴅᴀ ᴄʜᴇᴘᴜᴛʜᴜɴᴀᴅᴜ😄", 
    "ᴠᴇᴅɪ ᴀᴍᴍᴀ ɢᴜᴅʜᴀʟᴀ ʙᴏᴍʙ ᴅᴇɴɢᴀ", 
    "ɴᴇ ᴇᴠᴀ ᴋᴏᴊᴀ ɢᴜᴅʜᴀʟᴀ ɴᴀ sᴜʟɪ", 
    "𝗠𝗲 𝗮𝗸𝗸𝗮 𝗻𝗶 𝗺𝗲 𝗳𝗮𝗺𝗶𝗹𝘆 𝗹𝗶 𝗻𝗲 𝗱𝗲𝗻𝗴𝗮", 
    "𝗡𝗶 𝗮𝗺𝗺𝗮 𝗽𝘂𝗸𝘂 𝗿𝗮 𝗸𝗼𝗷𝗮", 
    "𝗡𝗲 𝗷𝗮𝘁𝗵𝗶 𝗽𝘂𝗸𝘂𝗹𝗮𝗻𝗮 𝗺𝗮𝗱𝗮", 
    "𝗞𝗼𝗷𝗮 𝗷𝗮𝘁𝗵𝗶 𝗿𝗮 𝗺𝗲𝗱𝗵𝗶 𝗺𝗲 𝗮𝗺𝗺𝗮 𝗱𝗵𝗶 𝗲𝗿𝗿𝗶 𝗽𝘂𝗸𝗮 🤣", 
    "𝗠𝗲 𝗮𝗯𝗯𝗮 𝗸𝗶 𝘀𝘂𝗹𝗶 𝗹𝗲𝗴𝗮 𝗽𝗼𝘁𝗵𝗲 𝗺𝗲 𝗮𝗺𝗺𝗮 𝗻𝗶 𝗻𝗲𝗻𝗲 𝗲𝘀𝗶𝗻𝗱𝗵𝗶 😌", 
    "𝗚𝘂𝗱𝗵𝗮 𝗽𝗮𝗴𝗮𝗹𝗮 𝗱𝗲𝗻𝗴𝗶 𝗴𝘂𝗱𝗵𝗮𝗹𝗮 𝗯𝗼𝗺𝗯 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝗮 😡", 
    "𝗠𝗲 𝗮𝗸𝗸𝗮 𝗻𝗶 𝗴𝗮𝗻𝗶 𝗺𝗲 𝗰𝗵𝗲𝗹𝗹𝗶 𝗻𝗶 𝗴𝗮𝗻𝗶 𝗼𝘆𝗼 𝗿𝗼𝗼𝗺 𝗽𝗮𝗺𝗽𝘂 𝗿𝗮 𝗷𝗮𝘁𝗵𝗶 𝗽𝘂𝗸𝘂𝗹𝘂𝗻𝗮 𝗺𝗮𝗱𝗮", 
    "𝗡𝗶 𝗷𝗮𝘁𝗵𝗶 𝘁𝗮𝗸𝘂𝘃𝗮 𝗻𝗮 𝗸𝗼𝗱𝗮𝗸𝗮", 
    "𝗠𝗲 𝗮𝗺𝗺𝗮 𝗴𝘂𝗱𝗵𝗮 𝗹𝗼 𝗲𝗱𝗶𝗹𝗶 𝗽𝗲𝘁𝗶 𝘀𝗮𝗺𝗯𝗮𝗿𝘂 𝗱𝗲𝗻𝗴𝗮", 
    "𝗡𝗲 𝗸𝗼𝗷𝗮 𝗽𝘂𝗸𝘂 𝗹𝗮 𝗻𝗮 𝘀𝘂𝗹𝗶", 
    "𝐌𝐞 𝐚𝐦𝐦𝐚 𝐧𝐢 𝐧𝐞𝐧𝐮 𝐝𝐞𝐧𝐠𝐢𝐭𝐡𝐞 𝐩𝐮𝐭𝐢𝐧𝐚 𝐧𝐚 𝐤𝐨𝐝𝐚𝐤𝐚 😡", 
    "𝐍𝐢 𝐚𝐦𝐦𝐚 𝐩𝐮𝐤𝐮", 
    "𝐍𝐢 𝐚𝐤𝐤𝐚 𝐩𝐮𝐤𝐮", 
    "𝐍𝐢𝐛𝐛𝐚 𝐤𝐚𝐭𝐡𝐚𝐥 𝐝𝐞𝐧𝐠𝐚𝐤𝐚", 
    "𝐏𝐨𝐫𝐚 𝐥𝐚𝐧𝐳𝐚𝐤𝐨𝐝𝐚𝐤𝐚", 
    "𝐍𝐞𝐞 𝐚𝐦𝐦𝐚𝐧𝐢 𝐝𝐡𝐞𝐧𝐠𝐚", 
    "𝐘𝐞𝐤𝐤𝐮𝐯𝐚 𝐦𝐚𝐭𝐥𝐚𝐝𝐢𝐭𝐡𝐞 , 𝐧𝐞 𝐩𝐞𝐥𝐥𝐚𝐦 𝐧𝐢 𝐲𝐞𝐠𝐚𝐫𝐞𝐬𝐢 𝐝𝐡𝐞𝐧𝐠𝐮𝐭𝐡𝐚... 𝐆𝐨𝐣𝐣𝐚 𝐥𝐚𝐧𝐳𝐚𝐤𝐨𝐝𝐚𝐤𝐚", 
    "𝐆𝐨𝐣𝐣𝐚 𝐩𝐮𝐤𝐨𝐝𝐚", 
    "𝐌𝐚𝐝𝐝𝐚 𝐠𝐮𝐝𝐮 𝐫𝐚 𝐩𝐮𝐤𝐚", 
    "𝐏𝐮𝐤𝐮 𝐧𝐚𝐚𝐤𝐮 😂", 
    "𝐒𝐮𝐥𝐥𝐢 𝐠𝐚 🙂", 
    "𝐃𝐡𝐞𝐧𝐠𝐞𝐢 𝐥𝐨𝐯𝐞𝐝𝐚𝐲 😍", 
    "𝐘𝐞𝐫𝐫𝐢 𝐩𝐮𝐤𝐨𝐝𝐚 🤣", 
    "𝐋𝐚𝐧𝐣𝐨𝐝𝐚𝐤𝐚", 
    "𝐍𝐢 𝐀𝐦𝐦𝐚 𝐩𝐮𝐤𝐥𝐚 𝐬𝐮𝐥𝐥𝐢", 
    "𝐆𝐮𝐝𝐝𝐚 𝐩𝐚𝐠𝐚𝐥 𝐝𝐞𝐧𝐠𝐮𝐭𝐡𝐚", 
    "𝐏𝐢𝐥𝐥𝐚 𝐥𝐚𝐧𝐣𝐨𝐝𝐚𝐤𝐚 𝐠𝐮𝐝𝐝𝐚 𝐦𝐮𝐬𝐤𝐨𝐧𝐢 𝐝𝐞𝐧𝐠𝐞", 
    "𝐍𝐢 𝐩𝐞𝐥𝐥𝐚𝐦 𝐩𝐮𝐤𝐥𝐚 𝐦𝐨𝐝𝐝𝐚 🍆 𝐥𝐚𝐧𝐣𝐨𝐝𝐚𝐤𝐚 𝐠𝐮𝐝𝐝𝐚 𝐦𝐮𝐬𝐤𝐨𝐧𝐢 𝐝𝐧𝐞𝐠𝐞 😂", 
    "𝐌𝐨𝐝𝐝𝐚 𝐠𝐮𝐝𝐮 𝐒𝐮𝐥𝐥𝐢𝐠𝐚 😂", 
    "𝐊𝐮𝐭𝐡𝐚 𝐩𝐚𝐠𝐚𝐥 𝐝𝐞𝐧𝐠𝐮𝐭𝐡𝐚 😏", 
    "𝐍𝐢 𝐩𝐢𝐥𝐥𝐚 𝐩𝐮𝐤𝐥𝐨 𝐧𝐚 𝐬𝐮𝐥𝐥𝐢 😏", 
    "𝘕𝘪 𝘈𝘮𝘮𝘢 𝘱𝘪𝘭𝘭𝘢 𝘬𝘶𝘵𝘩𝘢𝘭𝘰 𝘯𝘢 𝘮𝘰𝘥𝘥𝘢 😻", 
    "𝘔𝘰𝘥𝘥𝘢 𝘨𝘶𝘥𝘶 😏", 
    "𝘚𝘶𝘭𝘭𝘪 𝘬𝘰𝘴𝘪 𝘤𝘩𝘦𝘵𝘩𝘪𝘭𝘰 𝘱𝘦𝘥𝘵𝘩𝘢 𝘭𝘢𝘯𝘫𝘰𝘥𝘢𝘬𝘢 😝", 
    "𝘕𝘪 𝘫𝘢𝘵𝘩𝘪. 𝘕𝘪 𝘥𝘦𝘯𝘨𝘢 😏", 
    "𝘕𝘪 𝘷𝘰𝘵𝘵𝘢𝘭𝘶 𝘱𝘪𝘴𝘪𝘬𝘪 𝘬𝘰𝘫𝘫𝘢 𝘰𝘥𝘪𝘯𝘪 𝘤𝘩𝘦𝘴𝘪 𝘥𝘦𝘯𝘨𝘶𝘵𝘩𝘢 😏", 
    "𝘕𝘪 𝘈𝘮𝘮𝘢 𝘬𝘶𝘵𝘩𝘢𝘭𝘢 90 𝘮𝘮 𝘳𝘰𝘥𝘶 𝘭𝘢𝘯𝘫𝘰𝘥𝘢𝘬𝘢 😏", 
    "𝘎𝘶𝘥𝘥𝘢 𝘭𝘢 𝘯𝘢 𝘮𝘰𝘥𝘥𝘢 🤬", 
    "𝘚𝘢𝘭𝘦 𝘯𝘪 𝘢𝘬𝘬𝘢 𝘱𝘶𝘬𝘭𝘢 𝘴𝘶𝘭𝘭𝘪 😍", 
    "𝘕𝘦𝘦 𝘱𝘦𝘭𝘭𝘢𝘮 𝘯𝘪 𝘨𝘰𝘫𝘫𝘢 𝘷𝘢𝘢𝘢𝘭𝘭𝘶 𝘥𝘩𝘦𝘯𝘨𝘢", 
    "𝘕𝘦𝘦 𝘢𝘬𝘬𝘢𝘯𝘪 𝘥𝘩𝘦𝘯𝘨𝘢 😍", 
    "𝘕𝘦𝘦 𝘢𝘬𝘬𝘢 𝘱𝘶𝘬𝘶𝘭𝘰 𝘯𝘢 𝘮𝘢𝘥𝘥𝘢 ☺️", 
    "𝘕𝘦𝘦 𝘱𝘦𝘭𝘭𝘢𝘮 𝘱𝘶𝘬𝘶𝘭𝘰 𝘕𝘢𝘢 𝘮𝘢𝘥𝘥𝘢 😘", 
    "𝘓𝘢𝘯𝘫𝘰𝘥𝘢𝘬𝘢 𝘯𝘪 𝘢𝘬𝘬𝘢 𝘯𝘪 𝘥𝘦𝘯𝘨𝘢 😏", 
    "𝕹𝖎 𝕬𝖒𝖒𝖆 𝖕𝖚𝖐𝖑𝖆 𝖚𝖈𝖍𝖆 𝖕𝖔𝖘𝖎 𝖉𝖓𝖊𝖌𝖚𝖙𝖍𝖆 💋", 
    "𝗡𝗶 𝗮𝗸𝗸𝗮 𝗽𝗲𝗱𝗱𝗮 𝗹𝗮𝗻𝗷𝗮 𝗸𝗮𝗱𝗮 𝗔𝗱𝗮 𝗱𝗲𝗻𝗴𝗶𝗰𝗸𝘂𝗻𝘁𝘂𝗻𝗱𝗶 𝗮𝗻𝘁𝗮 𝗸𝗮𝗽𝗱𝘂𝗸𝗼 𝗽𝗼 𝗱𝗻𝗲𝗴𝗲💋", 
    "𝗡𝗶 𝗽𝗲𝗹𝗹𝗮𝗺 𝗽𝘂𝗸𝗹𝗮 𝗻𝗮 𝗺𝗼𝗱𝗱𝗮 💋", 
    "𝗡𝗶 𝗽𝗲𝗹𝗹𝗮𝗻𝗶 𝗴𝗮𝗻𝗴 𝗯𝗮𝗻𝗴 𝗲𝘀𝗶 𝗱𝗲𝗻𝗴𝗮 💋", 
    "𝗡𝗶 𝗮𝗸𝗸𝗮 𝗻𝗶 𝗱𝗲𝗻𝗴𝗶 𝗽𝗶𝗹𝗹𝗮𝗹 𝗽𝘂𝗱𝘁𝗮𝗿𝘂 𝗮𝗮𝗮 𝗽𝗶𝗹𝗹𝗮𝗻𝗶 𝗸𝘂𝗱𝗮 𝗻𝗮 𝗽𝗶𝗹𝗹𝗮𝘁𝗵𝗼 𝗱𝗻𝗲𝗴𝗶𝘀𝘁𝗮 𝗹𝗮𝗻𝗷𝗼𝗱𝗮𝗸𝗮 😍", 
    "𝗡𝗶 𝗔𝗺𝗺𝗮𝗻𝗶 𝗿𝗮𝗶𝗹𝘄𝗮𝘆 𝘁𝗿𝗮𝗰𝗸 𝗸𝗶 𝗲𝘀𝗶 𝗱𝗲𝗻𝗴𝗮 🔥", 
    "𝗡𝗶 𝗴𝘂𝗱𝗵𝗹𝗮𝗮 𝗼𝗶𝗹 𝗽𝗼𝘀𝗲 𝗱𝗲𝗻𝗴𝗮", 
    "𝗔𝗿𝗲𝘆 𝗮𝗽𝗽𝘂𝗱𝘂 𝘀𝗿𝘂𝗷𝗮𝗻𝗮 𝗰𝗮𝗹𝗹 𝗿𝗲𝗰𝗼𝗿𝗱 𝘃𝗮𝗰𝗵𝗶𝗻𝗱𝗵𝗶 𝗰𝗵𝘂𝗱𝘂 𝗮𝗱𝗵𝗶 𝗻𝗶 𝗮𝗸𝗸𝗮 𝗱𝗵𝗶 𝗮𝗻𝗮𝘁𝘁𝗮 𝗴𝗮 𝗸𝗮𝗻𝗶 𝗱𝗮𝗻𝗶 𝗽𝘂𝗸𝘂 𝗰𝗵𝘂𝘀𝗮 𝗮 𝗹𝗲𝗮𝗸𝘀 𝗹𝗼𝗼 𝗺 𝘂𝗻𝗱𝗵𝗶 𝗮𝗯𝗯𝗮 😍🥵", 
    "𝗔𝗿𝗲𝘆 𝗺𝗼𝗻𝗻𝗮 𝗻𝗶 𝗮𝗺𝗺𝗮 𝗻𝗶 𝗱𝗲𝗻𝗴𝗮 𝗿𝗮 🥵 𝗺 𝘂𝗻𝗱𝗵𝗶 𝗿𝗮 𝗹𝗮𝗻𝗷𝗮 𝗺𝘂𝗻𝗱𝗮 𝗮𝗱𝗵𝗶 𝗰𝗵𝗶𝗸𝗲𝘆 𝗰𝗵𝗶𝗸𝘂𝗱𝗶𝗸𝗶 𝗮𝗯𝗯𝗮 𝗺 𝗺𝗮𝘇𝗮 🤤🙈 𝗱𝗮𝗻𝗶 𝗱𝗲𝗻𝗴𝗶 𝗱𝗲𝗻𝗴𝗜 𝗯𝗼𝗿𝗲 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝘂𝗱𝗵𝗶 𝗮𝗻𝘂𝗸𝗼", 
    "𝗡𝗶 𝗮𝗸𝗸𝗮/𝗰𝗵𝗲𝗹𝗹𝗶 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝗲𝘆 𝗰𝗵𝘂𝗱𝘂 𝗮𝗱𝗵𝗶 𝗰𝗵𝗲𝘀𝗲 𝘀𝗼𝘂𝗻𝗱𝘀 𝗸𝗶 𝗺𝗮 𝘁𝗵𝗮𝗺𝗺𝘂𝗱𝘂 𝗸𝘂𝗱𝗮 𝘃𝗮𝗰𝗵𝗶 𝗱𝗲𝗻𝗴𝗮𝗱𝘂 🥵🥀", 
    "𝗟𝗮𝗻𝗷𝗮 𝗺𝘂𝗻𝗱𝗮 𝗸𝗶 𝗽𝘂𝘁𝘁𝗲 𝗼𝗱𝗮 𝗻𝗶 𝗮𝗸𝗸𝗮 𝗽𝘂𝗸𝘂 𝗹𝗮𝗮 𝗻𝗮 𝘀𝘂𝗹𝗶 😂", 
    "𝗡𝗶 𝗻𝗼𝘁𝗹𝗼 𝗻𝗮𝗱𝗶 𝘀𝗽𝗲𝗿𝗺 𝗽𝗼𝘆𝗮", 
    "𝗔𝗿𝗲𝘆 𝗻𝗶 𝗮𝗺𝗺𝗮 𝗽𝘂𝗸𝘂 𝗹𝗮𝗮 𝘀𝗲𝘀𝗮𝗺 𝗽𝗼𝘀𝗲 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝗮", 
    "𝗔𝗿𝗲𝘆 𝗻𝗶 𝗮𝗸𝗸𝗮 𝗽𝘂𝗸𝘂 𝗹𝗮𝗮 𝗯𝗲𝗲𝗿 𝗯𝗼𝘁𝘁𝗹𝗲 𝗲𝘀𝗲 𝗱𝗲𝗻𝗴𝗮 😂🥵", 
    "𝗡𝗶 𝗮𝗺𝗺𝗮 𝗮𝗿𝘃𝘂 𝘁𝗵𝗼 𝗽𝗮𝗱𝘂𝗸𝗼𝗻𝗶 𝗻𝗶𝗻𝗻𝘂 𝗸𝗮𝗻𝗻𝗮𝗱𝗮 𝗺𝗼 𝗸𝗮𝗻𝗶 𝗺 𝗰𝗵𝗶𝗹𝗹𝗮𝗿𝗮 𝗺𝘂𝗻𝗱𝗮𝗸𝗼𝗱𝘂𝗸𝘂𝗶𝘃𝗶 𝗽𝘂𝘁𝘁𝗮𝘃 𝗿𝗮 😂", 
    "𝗡𝗶 𝗷𝗮𝘁𝗵𝗶 𝗸𝗮𝗽𝗽𝗮𝗹𝗮 𝗻𝗮 𝗺𝗼𝗱𝗱𝗮 𝗺 𝗰𝗵𝗶𝗹𝗹𝗮𝗿𝗮 𝗷𝗮𝘁𝗵𝗜 𝗿𝗮 𝗻𝗲𝗱𝗶 😂", 
]


STICKER_SPAM = [
      "CAACAgUAAxkBAAEHw8Vj7iROtz9HWYVjBPpJHQ5wy1Y10QACIwMAAtNOkFRMieqkrKGs1y4E", 
      "CAACAgEAAxkBAAEHw8dj7iRScHeG8NdMh4WwmX2WipAcgwAC4QEAAs10eUZRd5xuVwtuHC4E", 
      "CAACAgUAAxkBAAEHw8lj7iRVhsDm8sydhvJ4xpJJAauhqQAC6AcAAmsPyFQmY-lwU66hUS4E", 
      "CAACAgUAAxkBAAEHw8tj7iRYi5RwCF2j6mZli_rHx2MyRAACqwIAAum9kFSd0t5coq_F-y4E", 
      "CAACAgEAAxkBAAEHw81j7iRf86SEpAQkLpjTPIX-GtXRQgACVAIAAiGjqEYplGHpwRhgWC4E", 
      "CAACAgEAAxkBAAEHw89j7iRmzmcS3L6wkbXM2X_TrdAy0AAClQEAAvV_sUYRppaIN1JCTi4E", 
      "CAACAgEAAxkBAAEHw9Fj7iRrrhzu0ApeWKt04fZou3_7EAAC2AEAAhOYOEeOqF8G-9bI9C4E", 
      "CAACAgEAAxkBAAEHw9Nj7iRyrMVjOxwW5nIwjGDLcFeLIgACYAIAAtJC2EUKzJr9hySQEC4E", 
      "CAACAgEAAxkBAAEHw9Vj7iR2QtcrxWuwyoRqXe391OC89wACTQIAAqnS4EUu4qTq35a3Py4E", 
      "CAACAgEAAxkBAAEHw9dj7iR6rChhPTxS0YpiYs-hF8tctwACNQIAAmsr4EVOmfqhDiFvdS4E", 
      "CAACAgEAAxkBAAEHw9lj7iR-h0gaJFCkDZmEQtIUvq8PWwACQwIAAt_8cUbyXtFYqZgJAi4E", 
      "CAACAgEAAxkBAAEHw9tj7iSEwrgMhNC35nujyTfnl-RXcQACugIAAqiBeUYHzFRVlW-nty4E", 
      "CAACAgEAAxkBAAEHw91j7iSLdloHt7qcdoD_03jive_22AAC6QEAAxp5RjBLE53bB4yBLgQ", 
      "CAACAgUAAxkBAAEHw99j7iSUQWuwAwULYSFijIDaiSIuAQACPQkAArDy4FUvJu9lrwyu_y4E", 
      "CAACAgUAAxkBAAEHw_Bj7isboM7VC_XAo8zLijMZGh5JZwACzgcAAiClSFcmyKmFrToUMS4E", 
      "CAACAgUAAxkBAAEHw_Jj7is6Is3MOhNVUhJlDOlIDQMdlwACdAgAAnx1SVdsK7fHnnJPKC4E" 
      "CAACAgUAAxkBAAEHw_Rj7is9ZDhAJ5cAAQG69ZE-NxFP2JkAAooIAAIfWElX7ovSqMCE8fsuBA", 
      "CAACAgUAAxkBAAEHw_Zj7itH-kBkEiYv892ikr7I6hy_6AACwwcAAiUHSFeiniGTe2hJci4E", 
      "CAACAgUAAxkBAAEHw_hj7itKQkIK4dHhR26EI25HxujLvAAC2QYAAv0-SFdLe4If4sTBZS4E", 
      "CAACAgUAAxkBAAEHw_pj7itQDHxVwtL0i74hqy3wR2s4xAACcAcAAt8ySVfm5O1GvCbARC4E", 
      "CAACAgUAAxkBAAEHw_xj7itTLOR8KC6KKH-ewl4PEJuTgQACAgsAAv0KSVe0eKEqPSnSui4E", 
      "CAACAgUAAxkBAAEHw_5j7itVFOdC5jrM0AHf1yc61fiDNgACrAgAAl_aSFdIJFwR6SWpOS4E", 
      "CAACAgUAAxkBAAEHxAABY-4rWL6bPKAuOR-728yad5sVK9YAAoAIAAKNLklX5LdKWsS6JTEuBA", 
      "CAACAgUAAxkBAAEHxAJj7itcf3VydzJiDwcY41uOXsV_DQACNAcAAuIRSFfFrwgt8_ZH2i4E", 
      "CCAACAgUAAxkBAAEHxARj7itf7t5QWZIvbSl4AAH1KelX5DkAApcIAAKDBGBXrciTM6VZr6QuBA", 
      "CAACAgUAAxkBAAEHxAZj7itj1u5v03hOdpUGaVaopCA-FQACzAcAAu-NYFd2GkzY2_3r4i4E", 
      "CAACAgUAAxkBAAEHxAhj7i2QDXFUNYHNkELrBJeSXD-9rAACwAMAAmBxkVQy1XpUDSn3iy4E", 
      "CAACAgUAAxkBAAEHxApj7i2bw5tT-EyP65HhOT25YaqwIgACfQMAAgI3kFTt3Q20S5Mz4i4E", 
      "CAACAgUAAxkBAAEHxAxj7i2gHJBxVAnNKGGa4CcAAc9bgJgAAnQCAALaQJBUL1T3Z1GWCTouBA", 
      "CAACAgUAAxkBAAEHxA5j7i2t5l4ZDkUpaw2X5sb0b88TkgACmAIAAtUjiVTMVzGjvgNrcS4E", 
      "CAACAgUAAxkBAAEHxBBj7i2yrw6eCE686p64gf0ahI2btAAC4wQAAqnukVSDkX9CcktBlC4E", 
      "CAACAgUAAxkBAAEHxBJj7i25MkEEac4iQ7eehZbEcLNZGwACYwIAAmXWkVTLrNGxi-fVYi4E", 
      "CAACAgUAAxkBAAEHxBRj7i3FNbT0V5sZDw0TUOHhnRXRjgACoAIAAmPMkFTZqd0SRuAF-i4E", 
      "CAACAgUAAxkBAAEHxBZj7i3UlCU1R8N4huTtdZNdBLtFVgACmAMAAiv1kFQlXGLIx0xh1S4E", 
      "CAACAgUAAxkBAAEHxBtj7i-6GFqYQ85UBkzAFBqrU51tDQACWAYAAiOgCFWYUB5_MZlRDy4E", 
      "CAACAgUAAxkBAAEHxB1j7i--3yvIC-I4oOv6lgOhF_B2ZwACjgcAAi85gFXHZqq2AQs9uC4E", 
      "CAACAgUAAxkBAAEHxB9j7i_Dw3QwWmwEJELBf5ghu9JgegAC3gcAAuCc0VVOU0wg7YUEvS4E", 
      "CAACAgUAAxkBAAEHxCFj7i_JAAE_Ybr5zSMQizWtfic2cMcAAoIHAAJcqNlVSZ-PzrwyltcuBA", 
      "CAACAgUAAxkBAAEHxCNj7i_ZbdfVbCFbYzAsbO4saB9lagACwAYAAhCwSVa4sYV_wZnBLy4E", 
      "CAACAgUAAxkBAAEHxCVj7i_miKK_u7WX6IiI-askUw0aDAACDQMAAnm-EVcC2xmhFv5grS4E", 
      "CAACAgUAAxkBAAEHxCdj7i_puknb6psgZpi5huYUo48P7AACkwMAAo6XUVczacPxGqNOYC4E", 
      "CAACAgUAAxkBAAEHxClj7i_66jEn7KmOvZ_w0yL1X0tB_wACagQAAliEAVQ2gYhMT-i8ui4E", 
]


PORN_STICK_SPAM = [
         "CAACAgUAAxkBAAEHxC5j7jDapsserqnMFHhM3iRWcKiE1gACawYAAm0BKVVk-yM3d-cjNC4E", 
         "CAACAgUAAxkBAAEHxC9j7jDaS6ESy7bmJFkN2AABYKazb7IAAmoFAAKkIChV8pjVuEw_CHQuBA", 
         "CAACAgUAAxkBAAEHxDBj7jDbisiOQxqlyOYG2w752YWjBAACPQcAAlYbKVWg4caqraKT7y4E", 
         "CAACAgUAAxkBAAEHxDJj7jDbKzR1nrpg58tdcoqlV3Ys5AACGwcAApMCIVWi8gtYyDwJCi4E", 
         "CAACAgUAAxkBAAEHxDNj7jDc-YLmF0RsGt2nurHnvGidcQACBQUAAkUGKVXMREAK0l1qqy4E", 
         "CAACAgUAAxkBAAEHxDRj7jDcKou0TmZCH6i9NAL7jeWS1wACOgoAAlp7KFWqVjz-TVjMVy4E", 
         "CAACAgUAAxkBAAEHxDZj7jDdtIJjTm6lNmvdWbhBOEcH1wACwwYAAil6IVWPG54AAcrJfrQuBA", 
         "CAACAgUAAxkBAAEHxDdj7jDdFgkJVBqN7EVYKzDosh6vKgACPQcAAlYbKVWg4caqraKT7y4E", 
         "CAACAgUAAxkBAAEHxDpj7jDeAtEVK1bobBk11M6rIAZjLAACBQUAAkUGKVXMREAK0l1qqy4E", 
         "CAACAgUAAxkBAAEHxDxj7jDgL50LNnmdIsWeNuPyC3x2-QACKQUAAlFwKFWEp0nH3G6ujy4E", 
         "CAACAgUAAxkBAAEHxD5j7jDgaTDmsTNOlSbLwiNTiwJ9LAACnwQAAqMGKVXhqZGH2mJb8y4E", 
         "CAACAgUAAxkBAAEHxD9j7jDg_amtvE135lD_5O2arGdcagACxAUAAsAbKVXJolc8jyN6sS4E", 
         "CAACAgUAAxkBAAEHxEFj7jDh8o8EdKlt90-WsMUtIJ3XTwACaQcAAhB0IVWIW8jfpIFTHi4E", 
         "CAACAgUAAxkBAAEHxEJj7jDhkDKFpfcxsB1KN-7j32zPzgACNgYAAlbsKFXMI9qRc0mg2i4E", 
         "CAACAgUAAxkBAAEHxERj7jDitREk9uOyVjZauT5mVgV8bgACKQUAAlFwKFWEp0nH3G6ujy4E", 
         "CAACAgUAAxkBAAEHxEVj7jDi643N4z3njR6zeJAwj1f9nQAC1wYAAgSVIVVN-dzYRz1Zpy4E", 
         "CAACAgUAAxkBAAEHxEdj7jDi7rtWHo-f5wOnb5Rh-eojVQACjwYAAv4TKFVlGQkzImcxOC4E", 
         "CAACAgUAAxkBAAEHxElj7jDj4CO5nf_Lp_AS6iQ7h17b3gACaQcAAhB0IVWIW8jfpIFTHi4E", 
         "CAACAgUAAxkBAAEHxEpj7jDjR3kwpeIBJsyLO9x-qvPLIAACTAcAAudZIVXT7gfGmjOVfS4E", 
         "CAACAgUAAxkBAAEHxE1j7jDlK68_L7l7RFR7G889vWRsPQACRQYAAhunIVV-D9LcPC95hy4E", 
         "CAACAgUAAxkBAAEHxE5j7jDmXNkbG3Zq60vMEFKSlzrMYgACIwUAAufBKVVJ2UM1B_ctJS4E", 
         "CAACAgUAAxkBAAEHxFBj7jDmZIzbtwNqIrSGgliFnyTLfwACOAoAAlolKVWF4aDW6iajWC4E", 
         "CAACAgUAAxkBAAEHxFFj7jDmbvlYXjjDi1J0NhX4Po9AlgACGwgAAupLKFW4-dCELqk8KC4E", 
         "CAACAgUAAxkBAAEHxFNj7jDnyY6VOYH-DEJ2X219N6G0OAACLwUAAi7EKVWCXtLu98TAlC4E", 
         "CAACAgUAAxkBAAEHxFRj7jDnO7lRRvOmdyK2dGBYNIWhIwAC_gQAApTPKFUdmLbnx6OiyS4E", 
         "CAACAgUAAxkBAAEHxFZj7jDoEUEPxbE3pIMoosx0cdi_4AACJwYAAj75KFWd48VsH9DdBy4E", 
         "CAACAgUAAxkBAAEHxFhj7jDoI08VjKWQ641gdIcVpLTeOAACoAcAAt_iIVVUIVeY07LV9y4E", 
         "CAACAgUAAxkBAAEHxFlj7jDp2oNqQ_oY3AXe0FXV_LSPpAACWgcAAvrpKVXbgpzZKgYQ3S4E",       
]
