class Car:
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_airbag_OK = is_airbag_ok
        self.is_painting_OK = is_painting_ok
        self.is_mechanic_OK = is_mechanic_ok
        Car.number_of_cars += 1
        Car.list_of_cars.append(self)

    def is_damaged(self):
        return not (self.is_airbag_OK and self.is_painting_OK and self.is_mechanic_OK)

    def get_info(self):
        print(f'{self.brand} {self.model}'.upper())
        print(f'Air Bag -ok- {self.is_airbag_OK}')
        print(f'Painting -ok- {self.is_painting_OK}')
        print(f'Mechanic -ok- {self.is_mechanic_OK}')
        print('-' * 60)


print('Class level variables BEFORE creating instances:',
      Car.number_of_cars, Car.list_of_cars)

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print('Class level variables AFTER creating instances:',
      Car.number_of_cars, Car.list_of_cars)
print('-------------------------------------------------------------------')

print('Id of class is: ', id(Car))
print('Id of instances are: ', id(car_01), id(car_02))
print('-------------------------------------------------------------------')

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type():', type(car_01) is Car)
print('Check the class of an object using __class__:', car_01.__class__)
print('-------------------------------------------------------------------')

print('List of instances attributes with values: ', vars(car_01))
print('-------------------------')
print('List of class attributes with values: ', vars(Car))
print('-------------------------------------------------------------------')

print('List of instance attribute with values: ', dir(car_01))
print('List of class attributes with values: ', dir(Car))

print('List of attributes taken from instance:', car_01.number_of_cars,
      '\nList of attributes taken from Class:', Car.number_of_cars)
