class Car:

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_airbag_OK = is_airbag_ok
        self.is_painting_OK = is_painting_ok
        self.is_mechanic_OK = is_mechanic_ok

    def is_damaged(self):
        return not (self.is_airbag_OK and self.is_painting_OK and self.is_mechanic_OK)

    def get_info(self):
        print(f'{self.brand} {self.model}'.upper())
        print(f'Air Bag -ok- {self.is_airbag_OK}')
        print(f'Painting -ok- {self.is_painting_OK}')
        print(f'Mechanic -ok- {self.is_mechanic_OK}')
        print('-' * 60)


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

car_01.get_info()
car_02.get_info()

print(car_01.brand, car_01.model, car_01.is_damaged())
print(car_02.brand, car_02.model, car_02.is_damaged())

print(car_01.brand, car_01.model, car_01.is_airbag_OK, car_01.is_painting_OK,
      car_01.is_mechanic_OK)
print(car_02.brand, car_02.model, car_02.is_airbag_OK, car_02.is_painting_OK,
      car_02.is_mechanic_OK)
