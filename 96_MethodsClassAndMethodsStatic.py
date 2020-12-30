import pickle
import glob

brandOnSale = 'Opel'


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

    def __get_is_on_sale(self):
        return self.__is_on_sale

    def __set_is_on_sale(self, new_is_on_sale_status):
        if self.brand == brandOnSale:
            self.__is_on_sale = new_is_on_sale_status
            print(f'Changing status is_on_sale to {new_is_on_sale_status} for {self.brand}')
        else:
            print(f'Cannot change status is_on_sale. Sale is able only for: {brandOnSale}')

    # we will write here the name of the variable by a big letter because we want to make this variable unique.
    IS_ON_SALE = property(__get_is_on_sale, __set_is_on_sale, None, 'if set to true, the car is available in sale')

    @classmethod
    def read_from_text(cls, a_text):
        a_new_car = cls(*a_text.split(':'))
        return a_new_car

    @staticmethod
    def convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def convert_KW_KM(KW):
        return KW * 1.36


line_of_text = 'Renault:Megane:True:True:False:False'
car_03 = Car.read_from_text(line_of_text)
car_03.get_info()
print('-------------------------------------------------------------------')

print('Converting 120 KM to KW', Car.convert_KM_KW(120))
print('Converting 90 KW to KM', Car.convert_KW_KM(90))
print('-------------------------------------------------------------------')

print(car_03.read_from_text(line_of_text))
print(car_03.convert_KW_KM(50))
print('-------------------------------------------------------------------')


# Lab

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair',
                   'christmas', 'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, wage, gluten_free=False, text=''):
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
        if self.kind == 'Cake' and text == '':
            self.__text = None
        elif self.kind == 'Cake':
            self.__text = text
        else:
            self.__text = "This baking is not a cake, and we can't add any birthday wishes."
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
        print(f'Text on the Cake: {self.text_properties}')

    def set_filling(self, add_filling):
        self.filling = add_filling

    def add_additives(self, add_more_additives):
        self.additives += add_more_additives

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'Cake':
            self.__text = new_text

    def save_to_file(self, path):
        pickle.dump(self, open(path, 'bw'))

    @classmethod
    def read_from_file(cls, path):
        new_pie = pickle.load(open(path, 'rb'))
        cls.bakery_offer.append(new_pie)
        return new_pie

    @staticmethod
    def get_bakery_files(catalog_name):
        print(glob.glob(f'{catalog_name}*.bakery'))

    text_properties = property(__get_text, __set_text, None, '''Some documentation about this property''')


cake_01 = Cake('Pear-Ginger Pie', 'Cake', 'Ginger',
               additives=['pears', 'crystallized ginger',
                          'orange juice', 'cinnamon'], filling='', wage=1.8)

cake_02 = Cake('Italian Rainbow', 'Biscuit', 'Raspberry jam', additives=[],
               filling='Layers of almond and coated in chocolate', wage=0.5, text='This is not a cake')

cake_03 = Cake('Banana Cream', 'Cake', 'Almond-Banana Cream',
               additives=['Almond cream', 'bananas',
                          'whipping cream'], filling='Covered whipping cream', wage=0.9, gluten_free=True)

cake_04 = Cake('Cocoa waffle', 'Waffle', 'Cocoa', [], 'Cocoa', 1.2)

cake_01.set_filling('Stuffed with pears')
cake_02.add_additives(['Almonds', 'raspberry jam', 'semisweet chocolate'])

print("Today's offer is:")
for number, elem in enumerate(Cake.bakery_offer):
    print('*' * 70)
    print(f'Number:{number + 1}')
    elem.show_info()
print('------------------------------------------------------------')

Cake.get_bakery_files('/home/darek/Projects/to_task_96/')
print('----------------------------------------------------------------')

cake_03.text_properties = 'Happy Birthday !!!!!!!!!!!!!!!!'
cake_04.text_properties = 'Enjoy'

cake_01.save_to_file(f'/home/darek/Projects/to_task_96/pickle_file_{cake_01.name}.bakery')
cake_02.save_to_file(f'/home/darek/Projects/to_task_96/pickle_file_{cake_02.name}.bakery')
cake_05 = Cake.read_from_file(f'/home/darek/Projects/to_task_96/pickle_file_{cake_02.name}.bakery')

print("Today's offer is:")
for number, elem in enumerate(Cake.bakery_offer):
    print('*' * 70)
    print(f'Number:{number + 1}')
    elem.show_info()
