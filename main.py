
from sample import create_samples
from manager import Manager
from sample import ApartmentRent, ApartmentSell, HouseRent, HouseSell, StoreRent, StoreSell
class handler:
    ADVERTISEMENT_TYPE = {
        1: ApartmentRent, 2: ApartmentSell,
        3: HouseRent, 4: HouseSell,
        # 4: StoreRent, 5: StoreSell
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    } 

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())
            for obj in adv.objects_list:
                print(obj.show_detail())

    def run(self):
        print("hello world")
        for key in self.SWITCHES:
            print(f"press {key} for {self.SWITCHES[key]}")
        user_input = input("Enter your choice: ")
        switch = self.SWITCHES.get(user_input, None)

        if switch is None:
            print("Invalid input")
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()
    handler = handler().run()
   
    # handler.run()
