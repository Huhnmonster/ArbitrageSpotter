import requests
import json
from Source import OrderPrototype

class Bitfinex:
    def __init__(self):
        self.ticker = "https://api.bitfinex.com/v1/pubticker/"
        self.symbols = "https://api.bitfinex.com/v1/symbols"
        self.symbol_list = []
        self.order_model = OrderPrototype.Order()

    def get_symbols(self):
        response =  requests.request("GET", self.symbols)
        self.symbol_list = response.text.strip('""[]').split('","')
        return self.symbol_list

    def get_products(self):
        self.get_symbols()
        for symbol in self.symbol_list[:20]:
            if symbol[3:] == "usd":
                try:
                    response = requests.request("GET", self.ticker + symbol)
                    product = json.loads(response.text)
                    self.order_model.add_product(symbol, "Bitfinex", product["last_price"], product["volume"])
                except KeyError:
                    pass
                    # logging here !!!!
        return self.order_model.return_products()