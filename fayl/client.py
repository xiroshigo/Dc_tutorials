from telethon import TelegramClient, events, sync

api_id = 7126991
api_hash = "1340841e6a51a2954c01530100b68559"
bot_token = "5521813666:AAFcdLdMqtN4UwF8DsuhsQEbVTEAp9SRees"

client = TelegramClient('dcTutorial', api_id, api_hash)
botClient = TelegramClient('dc_tutorials', api_id, api_hash).start(bot_token=bot_token)


