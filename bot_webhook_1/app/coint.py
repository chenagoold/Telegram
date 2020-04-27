import requests


def get_btc():
	url = 'https://yobit.net/api/2/btc_usd/ticker'
	response = requests.get(url).json()
	#print(r)
	#print(r['ticker']['last'])
	price = response['ticker']['last']
	return str(price) + ' USD' 

get_btc()