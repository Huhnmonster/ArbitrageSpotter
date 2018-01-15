import requests
import json
from collections import namedtuple

class Bitfinex:
    def __init__(self):
        self.ticker = "https://api.bitfinex.com/v1/pubticker/"
        self.symbols = "https://api.bitfinex.com/v1/symbols"
        self.symbol_list = []
        self.currency = namedtuple("Currency", ["symbol", "exchange", "price", "volume"])

    def get_symbols(self):
        response =  requests.request("GET", self.symbols)
        self.symbol_list = response.text.strip('""[]').split('","')
        return self.symbol_list

    def get_products(self):
        self.get_symbols()
        product_list = []
        for symbol in self.symbol_list[:20]:
            if symbol[3:] == "usd":
                try:
                    response = requests.request("GET", self.ticker + symbol)
                    product = json.loads(response.text)
                    product_list.append(self.currency(
                        symbol=symbol,
                        exchange="Bitfinex",
                        price=float(product["last_price"]),
                        volume=float(product["volume"])))
                except KeyError:
                    pass
                    # logging here !!!!
        return product_list