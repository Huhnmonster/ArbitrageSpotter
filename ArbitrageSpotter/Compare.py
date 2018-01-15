from ArbitrageSpotter import BitfenixTicker, BitstampTicker, GDAXTicker, CryptopiaTicker
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import itertools

class Compare:
    def __init__(self):
        self.bitfenix = BitfenixTicker.Bitfinex()
        self.gdax = GDAXTicker.GDAX()
        self.cryptopia = CryptopiaTicker.Cryptopia()
        self.bitstamp = BitstampTicker.Bitstamp()
        self.product_list = [
            self.bitfenix.get_products,
            self.gdax.get_products,
            self.bitstamp.get_products,
            self.cryptopia.get_products]
        self.products_to_check = [
            "btcusd",
            "ltcusd",
            "xrpusd",
            "ethusd",
            "bchusd"]

    def get_exchange_data(self):
        process_list = []
        exchange_data = []
        start = time.time()
        with ThreadPoolExecutor(max_workers=len(self.product_list)) as executor:
            process_list = [executor.submit(x) for x in self.product_list]
        exchange_data = [exchange.result() for exchange in as_completed(process_list)]
        end = time.time()
        print(end-start)
        return exchange_data

    def get_currency(self, data, symbol):
        currency_exchange_list = []
        for entry in itertools.chain.from_iterable(data):
            if entry.symbol == symbol:
                currency_exchange_list.append(entry)
        return currency_exchange_list

    def compare_prices(self):
        all_exchanges = self.get_exchange_data()
        for currency in self.products_to_check:
            _currency = self.get_currency(all_exchanges, currency)
            min_price = min(_currency, key= lambda x: x.price)
            max_price = max(_currency, key= lambda x: x.price)
            difference = max_price.price - min_price.price
            percentage = (1 - (min_price.price / max_price.price)) * 100
            print("Found a {:.2f} dollar difference ({:.2f}%) on {} between {} and {}!".format(
                difference, percentage, str.upper(currency), min_price.exchange, max_price.exchange))
        print(45*"-")

    

