from bittrex import BittrexClient
from bittrex import BittrexError


NOTIFY_PAIR = "USD-BTC"


def main():
	client = BittrexClient()
	current_price = client.get_last_price(pair=NOTIFY_PAIR)
	print("{} = {}".format(NOTIFY_PAIR, current_price))
	pass


if __name__ == '__main__':
	main()


