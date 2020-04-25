import requests
import misc
import json
from coint import get_btc
from time import sleep 


token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'


global last_update_id 
last_update_id = 0


def get_updates(): ## Метод 
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():
	data = get_updates()

	last_object = data['result'][-1]
	current_update_id = last_object['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id
		chat_id = data['result'][-1]['message']['chat']['id']
		message_text =  data['result'][-1]['message']['text']
		message = {'chat_id': chat_id,
		           'text': message_text}
		           #print(message_text)
		return message
	return None

def send_message(chat_id, text='Wait a second, please'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	#print(url)
	requests.get(url)


def main():
	#d = get_updates()
	#with open('updates.json', 'w' ) as file:
	#	json.dump(d, file, indent=2, ensure_ascii=False)
	#print(get_message())
	#send_message(13, 'hello worlds')
	while True: 
		answer = get_message()
		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			if text == '/btc':
				send_message(chat_id, get_btc())
		else:
			continue 


		sleep(3)





if __name__ == '__main__':
	main()

