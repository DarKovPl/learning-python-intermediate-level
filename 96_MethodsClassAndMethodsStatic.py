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
