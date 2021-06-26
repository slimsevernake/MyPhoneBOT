token = input('TOKEN: ')
admin_ids = input('Admin_ids: ').split(',')
admin_ids = [int(i) for i in admin_ids]

conf = f"TOKEN = '{token}'\nADMIN_IDS = {admin_ids}"
config = open('config.py', 'w')
config.write(conf)
config.close()

print(f'\nКонфиг записан:\n{conf}')


