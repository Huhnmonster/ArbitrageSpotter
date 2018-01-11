from Source import BitfenixTicker, GDAXTicker, CryptopiaTicker, BitstampTicker

class Compare:
    def __init__(self):
        self.Bitfenix = BitfenixTicker.Bitfinex()
        self.GDAX = GDAXTicker.GDAX()
        self.Cryptopia = CryptopiaTicker.Cryptopia()
        self.Bitstamp = BitstampTicker.Bitstamp()
        self.gdax_init_prices = self.GDAX.get_products()
        self.bitfenix_init_prices = self.Bitfenix.get_products()
        self.cryptopia_init_prices = self.Cryptopia.get_products()
        self.bitstamp_init_prices = self.Bitstamp.get_products()
        self.initial_polled_exchanges = [self.cryptopia_init_prices, self.bitstamp_init_prices, self.bitfenix_init_prices, self.gdax_init_prices]
        self.mode = 0
        self.threshhold = 0.0001

    def compare_prices(self):
        #First iteration
        price_list = {}
        if self.mode == 0:
            print(45*"-")
            for key in self.bitfenix_init_prices:
                # Instantiate List of all exchanges with corresponding price
                for exchange in self.initial_polled_exchanges:
                    if key in exchange:
                        price_list.update({exchange[key]["exchange"]:exchange[key]["price"]})
                # Get min and max price for each element
                if len(price_list) > 1:
                    min_price = min(price_list.items(), key=lambda x: x[1])
                    max_price = max(price_list.items(), key=lambda x: x[1])
                    # Print the difference
                    if 1 - (min_price[1] / max_price[1]) >= self.threshhold:
                        print("Biggest difference on {} found between {} and {}:{:2f} ({:2f}%)".format(key.upper(), max_price[0], min_price[0], max_price[1] - min_price[1], (1 - (min_price[1] / max_price[1]))*100))
                    else:
                        print("No opportunities found on {}! Waiting for new data".format(key.upper()))
                price_list = {}
            print(45*"-")
            self.mode = 1

        # Every iteration if i > 1
        elif self.mode == 1:
            #get new data
            gdax_prices = self.GDAX.get_products()
            bitfenix_prices = self.Bitfenix.get_products()
            cryptopia_prices = self.Cryptopia.get_products()
            bitstamp_prices = self.Bitstamp.get_products()
            exchange_polled = [gdax_prices, bitfenix_prices, cryptopia_prices, bitstamp_prices]
            for key in bitfenix_prices:
                # Instantiate List of all exchanges with corresponding price
                for exchange in exchange_polled:
                    if key in exchange:
                        price_list.update({exchange[key]["exchange"]:exchange[key]["price"]})
                # Get min and max price for each element
                if len(price_list) > 1:
                    min_price = min(price_list.items(), key=lambda x: x[1])
                    max_price = max(price_list.items(), key=lambda x: x[1])
                    # Print the difference
                    if 1 - (min_price[1] / max_price[1]) >= self.threshhold:
                        print("Biggest difference on {} found between {} and {}:{:2f} ({:2f}%)".format(key.upper(), max_price[0], min_price[0], max_price[1] - min_price[1], (1 - (min_price[1] / max_price[1]))*100))
                    else:
                        print("No opportunities found on {}! Waiting for new data".format(key.upper()))
                price_list = {}
            print(45*"-")        