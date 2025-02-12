from telethon.sync import TelegramClient

# Your API credentials
api_id = 123456  # Replace with your API ID
api_hash = '0946103600'  # Replace with your API Hash

# Create Telegram Client
client = TelegramClient('0946103600', api_id, api_hash)

# Connect to Telegram
with client:
    print("0946103600!")
