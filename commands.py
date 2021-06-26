import telebot
import checkAdmin
from config import *
from termux import API

bot = telebot.TeleBot(TOKEN)

def generic(message, userId):
	if not checkAdmin.c(userId):
		return

	try:
		message = message.replace('/c', '')
		if message == '':
			bot.send_message(userId, '🟡 Введите команду которую нужно выполнить: /с ls')
			return

		result = API.generic(message)
		result = f'🟢 Результат выполнения:\n{result[1]}\n\nКод ответа: {result[0]}\n\n\
		{result[2]}'
		bot.send_message(userId, result)
	except:
		bot.send_message(userId, '🔴 Ошибка...')
