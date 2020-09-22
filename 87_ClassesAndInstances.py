# class Car:
#     number_of_cars = 0
#     list_of_cars = []
#
#     def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok):
#         self.brand = brand
#         self.model = model
#         self.is_airbag_OK = is_airbag_ok
#         self.is_painting_OK = is_painting_ok
#         self.is_mechanic_OK = is_mechanic_ok
#         Car.number_of_cars += 1
#         Car.list_of_cars.append(self)
#
#     def is_damaged(self):
#         return not (self.is_airbag_OK and self.is_painting_OK and self.is_mechanic_OK)
#
#     def get_info(self):
#         print(f'{self.brand} {self.model}'.upper())
#         print(f'Air Bag -ok- {self.is_airbag_OK}')
#         print(f'Painting -ok- {self.is_painting_OK}')
#         print(f'Mechanic -ok- {self.is_mechanic_OK}')
#         print('-' * 60)
#
#
# print('Class level variables BEFORE creating instances:',
#       Car.number_of_cars, Car.list_of_cars)
#
# car_01 = Car('Seat', 'Ibiza', True, True, True)
# car_02 = Car('Opel', 'Corsa', True, False, True)
#
# print('Class level variables AFTER creating instances:',
#       Car.number_of_cars, Car.list_of_cars)
# print('-------------------------------------------------------------------')
#
# print('Id of class is: ', id(Car))
# print('Id of instances are: ', id(car_01), id(car_02))
# print('-------------------------------------------------------------------')
#
# print('Check if object belongs to class:', isinstance(car_01, Car))
# print('Check if object belongs to class using type():', type(car_01) is Car)
# print('Check the class of an object using __class__:', car_01.__class__)
# print('-------------------------------------------------------------------')
#
# print('List of instances attributes with values: ', vars(car_01))
# print('-------------------------')
# print('List of class attributes with values: ', vars(Car))
# print('-------------------------------------------------------------------')
#
# print('List of instance attribute with values: ', dir(car_01))
# print('List of class attributes with values: ', dir(Car))
#
# print('List of attributes taken from instance:', car_01.number_of_cars,
#       '\nList of attributes taken from Class:', Car.number_of_cars)
print('-------------------------------------------------------------------')


# Lab

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair',
                   'christmas', 'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, wage):
        self.name = name
        if str(kind).lower() in self.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.wage = wage
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(f'{self.name}'.upper())
        print('Kind:%21s' % self.kind)
        print('Taste:%20s' % self.taste)
        if self.additives > []:
            print(f"Additives:\n\t{'; '.join([str(add).capitalize() for add in self.additives])}")
        if self.filling > '':
            print(f'Filling:\n\t{self.filling}')
        print(f'Wage: {self.wage}')

    def set_filling(self, add_filling):
        self.filling = add_filling

    def add_additives(self, add_more_additives):
        self.additives += add_more_additives


cake_01 = Cake('Pear-Ginger Pie', 'Cake', 'Ginger',
               additives=['pears', 'crystallized ginger',
                          'orange juice', 'cinnamon'], filling='', wage=1.8)

cake_02 = Cake('Italian Rainbow', 'Biscuit', 'Raspberry jam', additives=[],
               filling='Layers of almond and coated in chocolate', wage=0.5)

cake_03 = Cake('Banana Cream', 'Cake', 'Almond-Banana Cream',
               additives=['Almond cream', 'bananas',
                          'whipping cream'], filling='Covered whipping cream', wage=0.9)

cake_04 = Cake('Cocoa waffle', 'Waffle', 'Cocoa', [], 'Cocoa', 1.2)


cake_01.set_filling('Stuffed with pears')
cake_02.add_additives(['Almonds', 'raspberry jam', 'semisweet chocolate'])

print("Today's offer is:")
for elem in Cake.bakery_offer:
    print('*' * 70)
    elem.show_info()
print('-------------------------------------------------------------------')

for obj in Cake.bakery_offer:
    print('----------------')
    print('Check if object belongs to class:', isinstance(obj, Cake))
    print('Check if object belongs to class:', type(obj) is Cake)
    print('----------------')
print(vars(cake_01), '\n' * 2, vars(Cake))
print('----------------')
print(dir(cake_01), '\n' * 2, dir(Cake))
