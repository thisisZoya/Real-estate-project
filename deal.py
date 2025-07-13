from base import BaseClass
from abc import ABC 
class Sell(ABC):
    def __init__(self, price_per_meter, discountable, convertable=False, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discount = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price: {self.price_per_meter}, discount: {self.discount}, convert: {self.convertable}")

class Rent(ABC):
    def __init__(self, initial_price, mounthly_price, convertable=False, discountable=False, *args, **kwargs):
        self.initial_price = initial_price
        self.mounthly_price = mounthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)
