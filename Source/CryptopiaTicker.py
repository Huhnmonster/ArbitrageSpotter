import requests
import json
from Source import OrderPrototype

class Cryptopia:
    def __init__(self):
        self.order_model = OrderPrototype.Order()
        self.api_endpoint = "https://www.cryptopia.co.nz/api/"

    def get_products(self):
        response = requests.request("GET", self.api_endpoint + "GetMarkets")
        products = json.loads(response.text)
        for product in products["Data"]:
            if product["Label"][4:] == "USDT":
                self.order_model.add_product(product["Label"].replace("/","").lower()[0:6], "Cryptopia", float(product["LastPrice"]), float(product["Volume"]))
        return self.order_model.return_products()
