# class Car:
#
#     def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, accessories):
#         self.brand = brand
#         self.model = model
#         self.is_airbag_OK = is_airbag_ok
#         self.is_painting_OK = is_painting_ok
#         self.is_mechanic_OK = is_mechanic_ok
#         self.accessories = accessories
#
#     def get_info(self):
#         print(f'{self.brand} {self.model}'.upper())
#         print(f'Air Bag     -ok-   {self.is_airbag_OK}')
#         print(f'Painting    -ok-   {self.is_painting_OK}')
#         print(f'Mechanic    -ok-   {self.is_mechanic_OK}')
#         print(f'Accessories        {self.accessories}')
#         print('-' * 60)
#
#     def __iadd__(self, other):
#         if type(other) is list:
#             accessories = self.accessories
#             accessories.extend(other)
#             return Car(self.brand, self.model, self.is_airbag_OK, self.is_painting_OK,
#                        self.is_mechanic_OK, self.accessories)
#         elif type(other) is str:
#             accessories = self.accessories
#             accessories.append(other)
#             return Car(self.brand, self.model, self.is_airbag_OK, self.is_painting_OK,
#                        self.is_mechanic_OK, self.accessories)
#         else:
#             raise Exception(f'Adding type {type(other)} to Car is not implemented')
#
#     def __add__(self, other):
#         if type(other) is Car:
#             return [self, other]
#         else:
#             raise Exception(f'Adding type {type(other)} to Car is not implemented')
#
#     def __str__(self):
#         return f"Brand: {self.brand}, Model: {self.model}"
#
#
# car_01 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
# car_01.get_info()
#
# car_01 += ['navigation system', 'roof rack']
# car_01.get_info()
#
# car_01 += 'loudspeaker'
# car_01.get_info()
#
# car_02 = Car('Opel', 'Corsa', True, False, True, [])
#
# car_pack = car_01 + car_02
# print(f'car_1 + car_2= {car_pack[0].brand, car_pack[1].brand}')
# print('------------------------------------------------------------')
# print(car_01)


# Lab

class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return 'Kind of the sweet:' + f' {self.kind}'.title() + f', name: {self.name}' \
                                                                f' and additives: {self.additives}'

    def __iadd__(self, other):
        if type(other) is str:
            self.additives.append(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        elif type(other) is list:
            self.additives.extend(other)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        else:
            raise Exception(f'This entered variable "{type(other)}" is not a correct type.')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
print(cake01)
print('---------------------------------------------------')

cake01.show_info()

print('---------------------------------------------------')
cake01 += 'mayo'
print(cake01)

print('---------------------------------------------------')
cake01 += ['chocolate', 'hazelnuts']
print(cake01)

# print('---------------------------------------------------')
# This is an improper type of variable.
# cake01 += 3
# print(cake01)
