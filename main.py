import telebot
import startBot
import photo
import mRecording
import stats
import copyPaste
import commands
import checkAdmin
from termux import API
from config import *
from setBrightness import setBrightness

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['photo'])
def sendPhoto(message):
	photo.makeSendPhoto(message.chat.id)

@bot.message_handler(commands=['record'])
def mRecord(message):
	mRecording.mRecord(message)

@bot.message_handler(commands=['stats'])
def pStats(message):
	stat = stats.phoneStats()
	stat.sendStats(message.chat.id)

@bot.message_handler(commands=['copy'])
def copy(message):
	copyPaste.copy(message.text, message.chat.id)

@bot.message_handler(commands=['paste'])
def paste(message):
	copyPaste.paste(message.chat.id)

@bot.message_handler(commands=['setBrightness'])
def brightness(message):
	setBrightness(message.text, message.chat.id)

@bot.message_handler(commands=['c'])
def command(message):
	commands.generic(message.text, message.chat.id)

@bot.message_handler(commands=['author'])
def author(message):
	bot.send_message(message.chat.id, 'ℹ️ Create by ELVIN\n\
		[My telegram channel](https://t.me/ARELDEV_CHANNEL)\n\
		[My telegram chat](https://t.me/AREL_CHAT)\n\
		[My site](https://areldev.ru)', parse_mode='markdown')

@bot.message_handler(commands=['start', 'help'])
def nCommand(message):
	if not checkAdmin.c(message.chat.id):
		return
	bot.send_message(message.chat.id, f'🟢 Команды бота: https://telegra.ph/Dokumentaciya-k-MyPhoneBOT-06-26')

@bot.message_handler(content_types=['text'])
def nCommand(message):
	if not checkAdmin.c(message.chat.id):
		return
	bot.send_message(message.chat.id, f'🟡 Я незнаю что ответить на {message.text}')


if __name__ == '__main__':
	startBot.botStarted()
	bot.infinity_polling()
