import asyncio
from santhuspam.modules import mongodb

collection = mongodb.pmpermit

PM_MESSAGE = (
    "[🥀 𝐇𝐢, 𝐈 𝐚𝐦 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐎𝐟 𝐀𝐦𝐚𝐥𝐚 , 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 😋 𝐦𝐲 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐂𝐡𝐚𝐭.    
    
🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐒𝐨𝐦𝐞𝐭𝐢𝐦𝐞 𝐔𝐧𝐭𝐢𝐥𝐥 𝐌𝐲 𝐁𝐨𝐬𝐬 𝐓𝐞𝐥𝐮𝐠𝐮 𝐜𝐨𝐝𝐞𝐫𝐬 😎 𝐢𝐬 𝐁𝐚𝐜𝐤 𝐓𝐨 𝐎𝐧𝐥𝐢𝐧𝐞, 𝐀𝐟𝐭𝐞𝐫 𝐓𝐡𝐚𝐭 𝐇𝐞 𝐖𝐢𝐥𝐥 𝐑𝐞𝐩𝐥𝐲 𝐘𝐨𝐮.    
    
😎 𝐏𝐥𝐞𝐚𝐬𝐞 𝐃𝐨𝐧'𝐭 𝐒𝐩𝐚𝐦 𝐇𝐞𝐫𝐞, 𝐄𝐥𝐬𝐞 𝐈 𝐖𝐢𝐥𝐥 𝐁𝐥𝐨𝐜𝐤 𝐘𝐨𝐮 🤟 𝐅𝐨𝐫 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐑𝐞𝐚𝐬𝐨𝐧𝐬, 𝐒𝐨 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 ✨ ...]"
)

BLOCKED = "**I know your spammer chutiya your getting to block bye!"

LIMIT = 5


async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        await collection.insert_one(doc)
    if not r2:
        await collection.insert_one(doc2)


async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})


async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PM_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    if not result["pmpermit"]:
        return False
    else:
        return True

