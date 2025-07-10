from base import BaseClass
from deal import Sell, Rent
from estate import Apartment, House, Store

class ApartmentSell(Apartment, Sell):
    def show_detail(self):
        self.show_description()
        Sell.show_price(self)

class ApartmentRent(BaseClass):
    pass

class HouseSell(BaseClass):
    pass

class HouseRent(BaseClass):
    pass

class StoreSell(BaseClass):
    pass

class StoreRent(BaseClass):
    pass
