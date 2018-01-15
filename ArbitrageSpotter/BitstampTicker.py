import json
import requests
from collections import namedtuple

class Bitstamp:
    def __init__(self):
        self.api_endpoint = "https://www.bitstamp.net/api/v2/"
        self.currency = namedtuple("Currency", ["symbol", "exchange", "price", "volume"])
        self.symbol_list = []

    def get_symbols(self):
        response = requests.request("GET", self.api_endpoint + "trading-pairs-info")
        symbols = json.loads(response.text)
        for symbol in symbols:
            self.symbol_list.append(symbol["url_symbol"])
        return self.symbol_list

    def get_products(self):
        product_list = []
        self.get_symbols()
        for symbol in self.symbol_list:
            if symbol[3:] == "usd" and symbol[:3] != "eur":
                response = requests.request("GET", self.api_endpoint + "ticker/" + symbol)
                product = json.loads(response.text)
                product_list.append(self.currency(
                    symbol=symbol,
                    exchange="Bitstamp",
                    price=float(product["last"]),
                    volume=float(product["volume"])))
        return product_list
