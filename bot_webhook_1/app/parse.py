import requests
from main import write_json
import re


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
	#print(get_price())
	print(get_price(parse_text('сколько стоит /eth_usd?')))
	#parse_text(' /btc_usd')

if __name__ == '__main__':
	main()
