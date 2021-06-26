import checkAdmin
import telebot
from config import TOKEN
from termux import API

bot = telebot.TeleBot(TOKEN)

class phoneStats:
	def batteryInfo(self):
		if API.battery()[0] == 0:
			batteryInformation = API.battery()
			percentage = batteryInformation[1]['percentage']
			temperature = batteryInformation[1]['temperature']
			health = batteryInformation[1]['health']
			status = batteryInformation[1]['status']
			current = batteryInformation[1]['current']
			sCurrent = 'Скорость разрядки: '
			if status == 'CHARGING':
				sCurrent = 'Скорость зарядки: +'

			return {'error':False, 
			'percentage':f'Заряд батареи: {percentage}%',
			'temperature':f'Температура батареи: {temperature}°C',
			'health':f'Состояние батареи: {health}',
			'status':f'Статус: {status}',
			'current':f'{sCurrent}{current}mA в час'
			}

		else:
			return {'error':True, 
			'errorCode':batteryInformation[0],
			'errorMessage':batteryInformation[1],
			}

	def volumeInfo(self):
		if API.volume()[0] == 0:
			volumeInformation = API.volume()
			callVolume = volumeInformation[1][0]['volume']
			systemVolume = volumeInformation[1][1]['volume']
			ringVolume = volumeInformation[1][3]['volume']
			notificationVolume = volumeInformation[1][5]['volume']
			maxVolume = volumeInformation[1][1]['max_volume']

			return {'error':False, 
			'systemVolume':f'Громкость системы: {systemVolume}/{maxVolume}',
			'callVolume':f'Громкость звонка: {callVolume}/{maxVolume}',
			'ringVolume':f'Громкость рингтона: {ringVolume}/{maxVolume}',
			'notificationVolume':f'Громкость уведомлений: {notificationVolume}/{maxVolume}',
			}

		else:
			return {'error':True,
			'errorCode':volumeInformation[0],
			'errorMessage':volumeInformation[1],
			}

	def wifiConnectionInfo(self):
		if API.generic('termux-wifi-connectioninfo')[0] == 0:
			wifiConnectInfo = API.generic('termux-wifi-connectioninfo')
			ip = 'No IP'
			if API.generic('curl https://api.myip.com')[0] == 0:
				ip = API.generic('curl https://api.myip.com')[1]['ip']
			localIp = wifiConnectInfo[1]['ip']
			speedMbps = wifiConnectInfo[1]['link_speed_mbps']
			macAddress = wifiConnectInfo[1]['mac_address']
			networkId = wifiConnectInfo[1]['network_id']

			return {'error':False,
			'ip':f'ip: {ip}',
			'localIp':f'Локальный ip: {localIp}',
			'speedMbps':f'Скорость wifi: {speedMbps}mbps',
			'macAddress':f'MAC адресс: {macAddress}',
			'networkId':f'Network ID: {networkId}',
			}

		else:
			return {'error':True, 
			'errorCode':wifiConnectInfo[0],
			'errorMessage':wifiConnectInfo[1],
			}

	def getAllStats(self):
		bInfo = self.batteryInfo()
		vInfo = self.volumeInfo()
		wInfo = self.wifiConnectionInfo()

		if not bInfo['error']:
			allStats =f"🔋 Информация о батарее 🔋\n\
{bInfo['percentage']}\n\
{bInfo['temperature']}\n\
{bInfo['health']}\n\
{bInfo['status']}\n\
{bInfo['current']}\n\n"

		if not vInfo['error']:
			allStats += f"🔊 Информация о громкости 🔊\n\
{vInfo['systemVolume']}\n\
{vInfo['callVolume']}\n\
{vInfo['ringVolume']}\n\
{vInfo['notificationVolume']}\n\n"

		if not wInfo['error']:
			allStats += f"📶 Информация о WIFI 📶\n\
{wInfo['ip']}\n\
{wInfo['localIp']}\n\
{wInfo['speedMbps']}\n\
{wInfo['macAddress']}\n\
{wInfo['networkId']}"

		return allStats

	def sendStats(self, userId):
		if not checkAdmin.c(userId):
			return

		bot.send_message(userId, self.getAllStats())
