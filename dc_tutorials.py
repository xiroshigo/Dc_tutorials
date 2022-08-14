#		telethon 3-dars
#userbot inlinequery button
#created .help plugin
#channel: @dc_tutorials

from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
import time

import fayl.client, fayl.help

client = fayl.client.clien
botClient = fayl.client.botClient

with client as darknetos:
			darknetos.add_event_handler(fayl.help.help)


client.start()
client.run_until_disconnected()