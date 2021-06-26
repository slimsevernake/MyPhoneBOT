import telebot 
import checkAdmin
from termux import API
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def paste(userId):
	if not checkAdmin.c(userId):
		return
	text = API.generic('termux-clipboard-get')
	bot.send_message(userId, f'Скопированный текст: `{text[1]}`', parse_mode='markdown')

def copy(text, userId):
	if not checkAdmin.c(userId):
		return
	text = text.replace('/copy', '')
	if text == '':
		bot.send_message(userId, '🟡 Введите текст который нужно скопировать: /copy тут текст')
		return

	result = API.generic(f'termux-clipboard-set {text}')
	if result[0] == 0:
		bot.send_message(userId, '🟢 Скопировано: ' + text)
	else:
		bot.send_message(userId, '🔴 Ошибка, возможно вы не выдали TermuxAPI нужные разрешения')