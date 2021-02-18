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


#  Lab

class Cake:

    def __init__(self, name, kind, taste, additives, filling, wage):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.wage = wage

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


cake_01 = Cake('Pear-Ginger Pie', 'Pie', 'Ginger',
               additives=['pears', 'crystallized ginger',
                          'orange juice', 'cinnamon'], filling='', wage=1.8)

cake_02 = Cake('Italian Rainbow', 'Cookies', 'Raspberry jam', additives=[],
               filling='Layers of almond and coated in chocolate', wage=0.5)

cake_03 = Cake('Banana Cream', 'Pie', 'Almond-Banana Cream',
               additives=['Almond cream', 'bananas',
                          'whipping cream'], filling='Covered whipping cream', wage=0.9)

bakery_offer = [cake_01, cake_02, cake_03]

cake_01.set_filling('Stuffed with pears')
cake_02.add_additives(['Almonds', 'raspberry jam', 'semisweet chocolate'])

print("Today's offer is:")
for elem in bakery_offer:
    print('*' * 70)
    elem.show_info()
