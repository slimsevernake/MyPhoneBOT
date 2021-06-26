import telebot 
import checkAdmin
from termux import API
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def setBrightness(text, userId):
	if not checkAdmin.c(userId):
		return

	try:
		brightness = int(text.replace('/setBrightness ', ''))
		if brightness < 0 or brightness > 255:
			bot.send_message(userId, '🟡 Яркость нельзя установить выше 255 или ниже 0')
			return
	except:
		brightness = 'auto'

	result = API.generic(f'termux-brightness {brightness}')
	if result[0] == 0:
		bot.send_message(userId, f'🟢 Яркость установлена на {brightness}')

	else:
		bot.send_message(userId, f'🔴 Ошибка, возможно вы не выдали Termux API все нужные разрешения.')
