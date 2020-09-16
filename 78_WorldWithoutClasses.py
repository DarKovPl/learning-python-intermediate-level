car_01 = {
    'car_brand': 'Seat',
    'car_model': 'Ibiza',
    'car_is_airbag_OK': True,
    'car_is_paintingOK': True,
    'car_is_mechanicOK': True
}
car_02 = {
    'car_brand': 'Opel',
    'car_model': 'Corsa',
    'car_is_airbag_OK': True,
    'car_is_paintingOK': False,
    'car_is_mechanicOK': True
}


def is_car_damaged(a_car):
    return not (a_car['car_is_airbag_OK'] and a_car['car_is_paintingOK']
                and a_car['car_is_mechanicOK'])


print(is_car_damaged(car_01))
print(is_car_damaged(car_02))

list_of_cars = [car_01, car_02]

for c in list_of_cars:
    print(f"{c['car_brand']} {c['car_model']} is damaged: {is_car_damaged(c)}")

# Lab
cake_1 = {
    'cake_taste': 'vanilia',
    'cake_glaze': 'chocolade',
    'cake_text': 'Happy Brithday',
    'cake_weight': 0.7
}

cake_2 = {
    'cake_taste': 'tee',
    'cake_glaze': 'lemon',
    'cake_text': 'Happy Python Coding',
    'cake_weight': 1.3
}


def show_cake_info(cake):
    print(f"{cake['cake_taste']} cake with {cake['cake_glaze']} glaze with text "
          f"'{cake['cake_text']}' of {cake['cake_weight']} kg")


cakes_list = [cake_1, cake_2]

for c in cakes_list:
    show_cake_info(c)
