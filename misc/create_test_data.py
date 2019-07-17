import requests
import pprint
import random

API_URL = 'http://localhost:8000/api/'
AUTH = ('ubuntu', 'password')


def add_user(f_name, l_name, is_staff):
    return requests.post(url=f"{API_URL}users/", data={
        "username": f"{f_name}-{l_name}",
        "is_staff": is_staff,
        "email": f"{f_name}.{l_name}@shoppinglist.com"
    }, auth=AUTH)


def add_shop(name, address, website):
    return requests.post(url=f"{API_URL}shops/", data={
        "name": name,
        "address": address,
        "website": website
    }, auth=AUTH)


def add_item(name, description, price, unit, barcode):
    return requests.post(url=f"{API_URL}items/", data={
        "name": name,
        "description": description,
        "price": price,
        "price_unit": unit,
        "barcode": barcode
    }, auth=AUTH)


def create_test_data():
    # Admin users
    for f in ['Ben', 'Dave', 'John', 'Brian', 'Geoff']:
        for l in ['Staff']:
            pprint.pprint(add_user(f, l, "true").text)

    ## non-staff users
    for f in ['Ben', 'Dave', 'John', 'Brian', 'Geoff', 'Lucy', 'Hannah', 'Amanda', 'Ruby']:
        for l in ['Jones', 'Smith', 'Mcaulney', 'Adams', 'Hartford', 'Magoo']:
            pprint.pprint(add_user(f, l, "false").text)

    streets = ['Arngle Blvd.', 'Testing Road']
    towns = ['Testsville', 'Tenessee', 'Test town']
    post = ['TF', 'SY', 'BE', 'N', 'M', 'W', 'GB', 'EN', 'WA']

    # Shops
    for x in range(20):
        pprint.pprint(add_shop(f'Test Shop {x}',
                               f"{random.Random().randint(1, 213)} {random.choice(streets)} {random.choice(towns)} "
                               f"{random.choice(post)}{random.randint(1, 7)}"
                               f" {random.choice(post)}{random.randint(0, 7)}",
                               "https://testshop.localhost"))

    # Items
    items = [('Snickers', 'Nuts n chocolate.', 0.45, '£'),
             ('Mars Bar', 'Chocolate and caramel stuff (oh and nougat)', 0.50, '£'),
             ('Malteasers', 'Floaty bubbles with a density < 1g/cm3', 0.76, '£'),
             ('Fruit Pastel', 'Fruity sweets, simple as', 1.00, '£'),
             ('Revels', 'Please, no more... lol', 1.50, '£')
             ]

    for item in items:
        pprint.pprint(
            add_item(item[0], item[1], item[2], item[3], 129345128).text)

    # Offers


    pprint.pprint('Done!')


if __name__ == "__main__":
    create_test_data()
