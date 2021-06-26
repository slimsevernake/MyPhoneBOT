import telebot
import checkAdmin
import time
from config import *
from termux import API

bot = telebot.TeleBot(TOKEN)

def mRecord(message):
	if not checkAdmin.c(message.chat.id):
		return

	API.generic('rm assets/record.mp3')
	try:
		duration = int(message.text.replace('/record', ''))
		if duration > 900 or duration < 1:
			bot.send_message(message.chat.id, '🟡 Запись не может длиться более 900 секунд(15 минут)\n\
				Или менее 1 секунды')
			return

		bot.send_message(message.chat.id, f'🕑 Запись будет готова через {duration} секунд')
		result = API.generic(f'termux-microphone-record -l {duration} -f assets/record.mp3')
		time.sleep(duration+2)
	except:
		bot.send_message(message.chat.id, '🕑 Запись будет готова через 5 секунд')
		result = API.generic(f'termux-microphone-record -l 5 -f assets/record.mp3')
		time.sleep(6)

	if result[0] == 0:
		resAudio = open('assets/record.mp3', 'rb')
		bot.send_voice(message.chat.id, resAudio)

	else:
		bot.send_message(message.chat.id, '🔴 Произошла некая ошибка, вожможно вы не выдали\
		 боту разрешение на использывание микрофона')

