from base import BaseClass

class Sell(BaseClass):
    def __init__(self, price_per_meter, discountable, convertable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price: {self.price_per_meter}, discount: {self.discount}, convert: {self.convertable}")

class Rent(BaseClass):
    def __init__(self, initial_price, mounthly_price, convertable, discountable, *args, **kwargs):
        self.initial_price = initial_price
        self.mounthly_price = mounthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)
