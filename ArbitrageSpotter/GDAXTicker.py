import requests
from collections import namedtuple
import json

class GDAX:
    def __init__(self):
        self.api_endpoint = "https://api.gdax.com/"
        self.symbol_list = []
        self.currency = namedtuple("Currency", ["symbol", "exchange", "price", "volume"])

    def get_symbols(self):
        response = requests.request("GET", self.api_endpoint + "products")
        products = json.loads(response.text)
        for product in products:
            self.symbol_list.append(product["id"])
        return self.symbol_list

    def get_products(self):
        product_list = []
        self.get_symbols()
        for symbol in self.symbol_list:
            if symbol == "BTC-USD" or symbol == "LTC-USD" or symbol == "ETH-USD" or symbol == "BCH-USD":
                response = requests.request("GET", self.api_endpoint + "products/" + symbol + "/ticker")
                product = json.loads(response.text)
                product_list.append(
                    self.currency(symbol=symbol.replace("-","").lower(), 
                    exchange="GDAX", 
                    price=float(product["price"]), 
                    volume=float(product["volume"])))
        return product_list