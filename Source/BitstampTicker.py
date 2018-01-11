import json
import requests
from Source import OrderPrototype

class Bitstamp:
    def __init__(self):
        self.api_endpoint = "https://www.bitstamp.net/api/v2/"
        self.order_model = OrderPrototype.Order()
        self.symbol_list = []

    def get_symbols(self):
        response = requests.request("GET", self.api_endpoint + "trading-pairs-info")
        symbols = json.loads(response.text)
        for symbol in symbols:
            self.symbol_list.append(symbol["url_symbol"])
        return self.symbol_list

    def get_products(self):
        self.get_symbols()
        for symbol in self.symbol_list:
            if symbol[3:] == "usd" and symbol[:3] != "eur":
                response = requests.request("GET", self.api_endpoint + "ticker/" + symbol)
                product = json.loads(response.text)
                self.order_model.add_product(symbol, "Bitstamp", float(product["last"]), float(product["volume"]))
        return self.order_model.return_products()
