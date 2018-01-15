import requests
import json
from collections import namedtuple

class Cryptopia:
    def __init__(self):
        self.currency = namedtuple("Currency", ["symbol", "exchange", "price", "volume"])
        self.api_endpoint = "https://www.cryptopia.co.nz/api/"

    def get_products(self):
        product_list = []
        response = requests.request("GET", self.api_endpoint + "GetMarkets")
        products = json.loads(response.text)
        for product in products["Data"]:
            if product["Label"][4:] == "USDT":
                product_list.append(self.currency(
                    symbol=product["Label"].replace("/","").lower()[0:6],
                    exchange="Cryptopia",
                    price=float(product["LastPrice"]),
                    volume=float(product["Volume"])))
        return product_list
