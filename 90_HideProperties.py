class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale):
        self.brand = brand
        self.model = model
        self.is_airbag_OK = is_airbag_ok
        self.is_painting_OK = is_painting_ok
        self.is_mechanic_OK = is_mechanic_ok
        self.__is_on_sale = is_on_sale
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)

    def is_damaged(self):
        return not (self.is_airbag_OK and self.is_painting_OK and self.is_mechanic_OK)

    def get_info(self):
        print(f'{self.brand} {self.model}'.upper())
        print(f'Air Bag -ok- {self.is_airbag_OK}')
        print(f'Painting -ok- {self.is_painting_OK}')
        print(f'Mechanic -ok- {self.is_mechanic_OK}')
        print(f'Is on sale? {self.__is_on_sale}')
        print('-' * 60)


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

car_02.is_on_sale = False
car_02.year_of_production = 2005
del car_02.year_of_production

setattr(car_02, 'TAXI', False)
delattr(car_02, 'TAXI')
print(hasattr(car_02, 'TAXI'))

car_02.get_info()
print(vars(car_02))
