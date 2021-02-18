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

# Lab

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair',
                   'christmas', 'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, wage, gluten_free=False):
        self.name = name
        if str(kind).lower() in self.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.wage = wage
        self.__gluten_free = gluten_free
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
        print('This product is gluten free' if self.__gluten_free else 'This product has gluten')

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
                          'whipping cream'], filling='Covered whipping cream', wage=0.9, gluten_free=True)

cake_04 = Cake('Cocoa waffle', 'Waffle', 'Cocoa', [], 'Cocoa', 1.2)


cake_01.set_filling('Stuffed with pears')
cake_02.add_additives(['Almonds', 'raspberry jam', 'semisweet chocolate'])

print("Today's offer is:")
for elem in Cake.bakery_offer:
    print('*' * 70)
    elem.show_info()


cake_03.__gluten_free = False
print(dir(cake_03))
cake_03._Cake__gluten_free = False
cake_03.show_info()

