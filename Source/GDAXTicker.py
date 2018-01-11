import requests
from Source import OrderPrototype
import json

class GDAX:
    def __init__(self):
        self.api_endpoint = "https://api.gdax.com/"
        self.symbol_list = []
        self.order_model = OrderPrototype.Order()

    def get_symbols(self):
        response = requests.request("GET", self.api_endpoint + "products")
        products = json.loads(response.text)
        for product in products:
            self.symbol_list.append(product["id"])
        return self.symbol_list

    def get_products(self):
        self.get_symbols()
        for symbol in self.symbol_list:
            if symbol == "BTC-USD" or symbol == "LTC-USD" or symbol == "ETH-USD" or symbol == "BCH-USD":
                response = requests.request("GET", self.api_endpoint + "products/" + symbol + "/ticker")
                product = json.loads(response.text)
                self.order_model.add_product(symbol.replace("-","").lower(), "GDAX", product["price"], product["volume"])
        return self.order_model.return_products()