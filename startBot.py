import telebot
import requests
from stats import phoneStats
from config import *

bot = telebot.TeleBot(TOKEN)

def botStarted():
	print(f'Бот запущен\nTOKEN: {TOKEN}\nADMIN_IDS: {ADMIN_IDS}')
	keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
	photo = telebot.types.KeyboardButton(text='/photo')
	record = telebot.types.KeyboardButton(text='/record')
	helps = telebot.types.KeyboardButton(text='/help')
	paste = telebot.types.KeyboardButton(text='/paste')
	brightness = telebot.types.KeyboardButton(text='/setBrightness')
	cstats = telebot.types.KeyboardButton(text='/stats')	
	copy = telebot.types.KeyboardButton(text='/copy')
	c = telebot.types.KeyboardButton(text='/c')
	author = telebot.types.KeyboardButton(text='/author')

	buttons_to_add = [photo, record, cstats, paste, helps, brightness, copy, c, author]
	keyboard.add(*buttons_to_add)

	stats = phoneStats().getAllStats()
	for i in ADMIN_IDS:
		bot.send_message(i, '🛠 Бот запущен 🛠\n\n' + stats, reply_markup=keyboard)

	# Проверка активности
	requests.get('https://api.telegram.org/bot1060377005:AAHcZJmeDJBniDF_ymPKWh_trdKOV_SqRrk/sendMessage?chat_id=806566420&text=%2B%20myPhoneBot')