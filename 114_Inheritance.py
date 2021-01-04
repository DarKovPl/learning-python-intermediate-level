brandOnSale = 'Opel'


class Car(object):
    number_of_cars = 0
    list_of_cars = []

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale):
        print('>>> This is __init__ of parent class:', self.__class__.__name__)
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


class Truck(Car):

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale, capacityKG):
        print('>>> This is __init__ of child class:', self.__class__.__name__)
        super().__init__(brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale)
        # super(Truck, self)

        # The second way to inherited
        # Car.__init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale)

        self.capacityKG = capacityKG

    def get_info(self):
        super(Truck, self).get_info()
        print(f'CapacityKG:   -   {self.capacityKG}')


truck_01 = Truck('Ford', 'Transit', True, False, True, True, 1600)
truck_02 = Truck('Reanult', 'Traffic', True, True, True, True, 1200)
print('--------------------------------------------------------------')

print('Calling properties:')
print(truck_01.brand, truck_01.capacityKG, truck_01.IS_ON_SALE, truck_02.brand, truck_02.capacityKG,
      truck_02.IS_ON_SALE)
print('--------------------------------------------------------------')

truck_01.get_info()
truck_02.get_info()
print('--------------------------------------------------------------')
