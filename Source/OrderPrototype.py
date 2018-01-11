class Order:
    def __init__(self):
        self.exchange_products = {}

    def add_product(self, currency_pair, exchange, price, volume):
        self.exchange_products[currency_pair] = {"exchange":exchange, "price":float(price), "volume":float(volume)}

    def return_products(self):
        return self.exchange_products
    