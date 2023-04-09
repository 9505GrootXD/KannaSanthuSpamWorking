from config.config import API_ID, API_HASH, STRING_SESSION
from pyrogram import Client, idle


CLIENTS = []

for STRING_SESSION in STRING_SESSION:
    if STRING_SESSION:
        client = Client(
            session_name=STRING_SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="santhuspam.modules"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("tgshadow_fighters")
            CLIENT.join_chat("Telugucodersupdates")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("💞ʏᴏᴜʀ ᴀᴍᴀʟᴀ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛs ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 💞")
    idle()
