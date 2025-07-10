from user import User
from random import choice

FIRST_NAMES = ['John', 'Jane', 'Jim', 'Jill']
LAST_NAMES = ['Doe', 'Smith', 'Williams', 'Brown']
PHONE_NUMBERS = ['1234567890', '0987654321', '1234123456', '4567845678']

if __name__ == '__main__':
    for mobile in PHONE_NUMBERS:
        User(choice(FIRST_NAMES), choice(LAST_NAMES), mobile)

    for user in User.objects_list:
        print(f"{user._id}\t {user.full_name}")
