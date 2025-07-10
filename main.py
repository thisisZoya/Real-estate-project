from logging import root
from user import User
from random import choice
from estate import Apartment, House, Store
from region import Region
from advertisement import ApartmentRent, ApartmentSell, HouseRent, HouseSell, StoreRent, StoreSell


FIRST_NAMES = ['John', 'Jane', 'Jim', 'Jill']
LAST_NAMES = ['Doe', 'Smith', 'Williams', 'Brown']
PHONE_NUMBERS = ['1234567890', '0987654321', '1234123456', '4567845678']

if __name__ == '__main__':
    for mobile in PHONE_NUMBERS:
        User(choice(FIRST_NAMES), choice(LAST_NAMES), mobile)

    for user in User.objects_list:
        print(f"{user._id}\t {user.full_name}")

    reg1 = Region(name='Tashkent')
    apt1 = Apartment(user=User.objects_list[0],
                     area=100,
                     floor=2,
                     rooms_count=2,
                     built_year=2020,
                     region=reg1,
                     address='Tashkent, Amir Temur street, 123',
                     has_elevator=True,
                     has_parking=True)
    apt1.show_description()

    house1 = House(user=User.objects_list[1],
                   area=100,
                   floors_count=2,
                   rooms_count=2,
                   built_year=2020,
                   region=reg1,
                   address='Tashkent, Amir Temur street, 123',
                   has_yard=True)
    house1.show_description()
    
    store1 = Store(user=User.objects_list[2],
                   area=100,
                   rooms_count=2,
                   built_year=2020,
                   region=reg1,
                   address='Tashkent, Amir Temur street, 123')
    store1.show_description()

    apartment_sell = ApartmentSell(user=User.objects_list[2],
                     area=100,
                     floor=2,
                     rooms_count=2,
                     built_year=2020,
                     region=reg1,
                     address='Tashkent, Amir Temur street, 123',
                     has_elevator=True,
                     has_parking=True,
                     price_per_meter=10000,
                     discountable=True,
                     convertable=True)
    apartment_sell.show_detail()
