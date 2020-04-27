from flask import Flask  #1
from  flask import request
from flask_sslify import SSLify #5
from flask import jsonify
import requests 
import misc
import json
import re


app  = Flask(__name__) #2
SSLify = SSLify(app)  #6




token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'



def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f , indent = 2, ensure_ascii = False)


def get_updates():
	url = URL + 'getUpdates'
	r = requests.get(url)
	#write_json(r.json())
	return r.json()

def send_message(chat_id, text='Yes-yes'):
	url = URL + 'sendMessage'
	answer = {'chat_id': chat_id, 'text':text}
	r = requests.post(url, json=answer)
	return r.json()


def parse_text(text):
	pattern = r'/\w+'
	crypto = re.search(pattern, text).group()
	return crypto[1:]
	#print(crypto)

def get_price(crypto):
	url = 'https://yobit.net/api/2/{}/ticker'.format(crypto)
	r = requests.get(url).json()
	price = r['ticker']['last']
	return price
	#write_json(r.json(), filename='price.json')








def main():
	#r = requests.get(URL + 'getMe')
	#print(r.json())
	#write_json(r.json())
	#r = get_updates()
	#chat_id = r['result'][-1]['message']['chat']['id']
	#send_message(chat_id)
	pass








@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		r = request.get_json()
		chat_id = r['message']['chat']['id']
		message = r['message']['text']
		#write_json(r)
		#return jsonify(r)
		pattern = r'/\w+'
		if re.search(pattern, message):
			price = get_price(parse_text(message))
			send_message(chat_id, text=price)

	return '<h1>Hello World</h1>' 

if __name__ == '__main__': #3
	#app.run() #4
	#main()
	app.run()