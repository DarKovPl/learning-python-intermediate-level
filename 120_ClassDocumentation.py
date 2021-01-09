brandOnSale = 'Opel'


class Car:
    """
    Car - class operating on cars available in the dealer
    """
    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale):
        """
        :param brand: the brand of the car i.e Fiat
        :param model:the model of the car i.e Multipla
        :param is_airbag_ok: is the airbag not used
        :param is_painting_ok: is the car paint original/no corrections
        :param is_mechanic_ok: is the car free of any mechanics failure
        :param is_on_sale: is the car covered extra promotion
        """
        self.brand = brand
        self.model = model
        self.is_airbag_OK = is_airbag_ok
        self.is_painting_OK = is_painting_ok
        self.is_mechanic_OK = is_mechanic_ok
        self.__is_on_sale = is_on_sale

    @property
    def is_on_sale(self):
        """is_on_sale- the car is on extra promotion that is limited in time
        (only selected cars may be on sale)"""
        return self.__is_on_sale

    @is_on_sale.setter
    def is_on_sale(self, new_is_on_sale_status):
        if self.brand == brandOnSale:
            self.__is_on_sale = new_is_on_sale_status
            print(f'Changing status is_on_sale to {new_is_on_sale_status} for {self.brand}')
        else:
            print(f'Cannot change status is_on_sale. Sale is able only for: {brandOnSale}')

    @is_on_sale.deleter
    def is_on_sale(self):
        self.__is_on_sale = None

    @property
    def car_title(self):
        return f'Mark: {self.brand}  Model: {self.model}'.title()


car_01 = Car('Seat', 'Ibiza', True, True, True, False)

help(Car)
print('-' * 60)

help(Car.is_on_sale)
