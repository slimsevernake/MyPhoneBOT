import telebot
from config import *
bot = telebot.TeleBot(TOKEN)

def c(userId):
	for i in ADMIN_IDS:
		if userId == i:
			return True

	bot.send_message(userId, '🔴 Доступ запрещен 403')
	return False