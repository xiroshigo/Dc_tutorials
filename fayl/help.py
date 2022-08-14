from telethon import TelegramClient, events, sync, functions, types, Button

import fayl.client
client = fayl.client.client
botClient = fayl.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "help":
								result = query.builder.article('Help', text = "~~DC TUTORIALS, DEVELOPERS CLUB~~", buttons= [
								[Button.inline("3-mavzu", data=b"1")],
								[Button.url("Tg channel", url="https://t.me/dc_tutorials")]
								
								])
								await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
								await event.answer("InlineKeyboardButton successor", alert=True)

@events.register(events.NewMessage(pattern=".help"))
async def help(event):
				results = await client.inline_query("@dc_tutorials_bot", "help")
				await results[0].click(event.chat_id)
				await event.message.delete()