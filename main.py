from pyrogram import Client, filters
import os

# Bot Setup
API_ID = 28039410
API_HASH = "a04aefebfd6955d64ce0197e4ca18bb6"
BOT_TOKEN = "7639988688:AAGn9_cP225P9YC7fdn8MPRQvlYmvK_fhWk"

app = Client(
    "file_reuploader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# /start command
@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("Hello!\n\nSend me any file (forwarded or uploaded), and I'll re-upload it freshly without any watermark or tag.")

# Handling all file types
@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def file_handler(client, message):
    m = await message.reply_text("Downloading your file...")
    file_path = await message.download()
    await m.edit("Uploading file without watermark...")

    if message.document:
        await message.reply_document(file_path)
    elif message.video:
        await message.reply_video(file_path)
    elif message.audio:
        await message.reply_audio(file_path)
    elif message.photo:
        await message.reply_photo(file_path)

    await m.delete()
    os.remove(file_path)  # Clean up downloaded file

app.run()
