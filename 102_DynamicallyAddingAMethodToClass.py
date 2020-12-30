import csv
import types
import pickle
import glob


# def export_to_file_static(path, header, data):
#     with open(path, 'w') as file:
#         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(header)
#         writer.writerow(data)
#     # just to see that the function was indeed called:
#     print('>>> This is function export_to_file - static method')
#
#
# def export_to_file_class(cls, path):
#     with open(path, 'w') as file:
#         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(['Brand', 'Model', 'IS_ON_SALE'])
#         for c in cls.list_of_cars:
#             writer.writerow([c.brand, c.model, c.IS_ON_SALE])
#     # just to see that the function was indeed called:
#     print('>>> This is function export_to_file - class method')
#
#
# def export_to_file_instance(self, path):
#     with open(path, 'w') as file:
#         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(['Brand', 'Model', 'IS_ON_SALE'])
#         writer.writerow([self.brand, self.model, self.IS_ON_SALE])
#     # just to see that the function was indeed called:
#     print('>>> This is function export_to_file - Instance method')
#
#
# brandOnSale = 'Opel'
#
#
# class Car:
#     number_of_cars = 0
#     list_of_cars = []
#
#     def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok, is_on_sale):
#         self.brand = brand
#         self.model = model
#         self.is_airbag_OK = is_airbag_ok
#         self.is_painting_OK = is_painting_ok
#         self.is_mechanic_OK = is_mechanic_ok
#         self.__is_on_sale = is_on_sale
#
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
#         print(f'Is on sale? {self.__is_on_sale}')
#         print('-' * 60)
#
#     def __get_is_on_sale(self):
#         return self.__is_on_sale
#
#     def __set_is_on_sale(self, new_is_on_sale_status):
#         if self.brand == brandOnSale:
#             self.__is_on_sale = new_is_on_sale_status
#             print(f'Changing status is_on_sale to {new_is_on_sale_status} for {self.brand}')
#         else:
#             print(f'Cannot change status is_on_sale. Sale is able only for: {brandOnSale}')
#
#     # we will write here the name of the variable by a big letter because we want to make this variable unique.
#     IS_ON_SALE = property(__get_is_on_sale, __set_is_on_sale, None, 'if set to true, the car is available in sale')
#
#
# car_01 = Car('Seat', 'Ibiza', True, True, True, False)
# car_02 = Car('Opel', 'Corsa', True, False, True, True)
#
# print('Static---------' * 10)
#
# Car.export_to_file_static = export_to_file_static
# # export_to_file_static(rf'/home/darek/Projects/to_task_102/{export_to_file_static.__name__}',
# #                       ['Brand', 'Model', 'IS_ON_SALE'], [car_01.brand, car_01.model, car_01.IS_ON_SALE])
# Car.export_to_file_static(rf'/home/darek/Projects/to_task_102/{Car.export_to_file_static.__name__}',
#                                 ['Brand', 'Model', 'IS_ON_SALE'], [car_01.brand, car_01.model, car_01.IS_ON_SALE])
# print(dir(Car))
# print('Class---------' * 10)
#
# # Car.export_to_file_class = export_to_file_class
# Car.export_to_file_class = types.MethodType(export_to_file_class, Car)
# Car.export_to_file_class(path=rf'/home/darek/Projects/to_task_102/{Car.export_to_file_class.__name__}')
# print(dir(Car))
# print('Instance---------' * 10)
#
# # car_01.export_to_file_instance = export_to_file_instance
# car_01.export_to_file_instance = types.MethodType(export_to_file_instance, car_01)
# car_01.export_to_file_instance(path=rf'/home/darek/Projects/to_task_102/{car_01.export_to_file_instance.__name__}')
# print(dir(car_01))
# print('-' * 50)
#
# if hasattr(car_01, 'export_to_file_static') and callable(car_01.export_to_file_static):
#     print('The object has method: export_to_file_static')
# if hasattr(car_01, 'export_to_file_class') and callable(car_01.export_to_file_class):
#     print('The object has method: export_to_file_class')
# if hasattr(car_01, 'export_to_file_instance') and callable(car_01.export_to_file_instance):
#     print('The object has method: export_to_file_instance')
# if hasattr(car_01, 'export_to_file_instancexxx') and callable(car_01.export_to_file_instance):
#     print('The object has method: export_to_file_instance')
# else:
#     print('No such method!!')


#  Lab

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cake_to_html_class(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for obj in cls.bakery_offer:
            content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
            f.write(content)


def export_all_cake_to_html_instance(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for num, obj in enumerate(self.bakery_offer):
            content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
            f.write(content)


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
        print(f'Text on the Cake: {self.set_text}')

    def set_filling(self, add_filling):
        self.filling = add_filling

    def add_additives(self, add_more_additives):
        self.additives += add_more_additives

    @property
    def set_text(self):
        return self.__text

    @set_text.setter
    def set_text(self, new_text):
        if self.kind == 'Cake':
            self.__text = new_text

    def save_to_file(self, path):
        pickle.dump(self, open(path, 'bw'))

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'br') as f:
            new_pie = pickle.load(f)
        cls.bakery_offer.append(new_pie)
        return new_pie

    @staticmethod
    def get_bakery_files(catalog_name):
        print(glob.glob(f'{catalog_name}*.bakery'))


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
cake_03.set_text = 'Happy Birthday !!!!!!!!!!!!!!!!'
cake_02.save_to_file(f'/home/darek/Projects/to_task_96/pickle_file_{cake_02.name}.bakery')
cake_05 = Cake.read_from_file(f'/home/darek/Projects/to_task_96/pickle_file_{cake_02.name}.bakery')
print('-' * 60)

# Here we are exporting the first cake from the list of our bakery into the html file using a static method.
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(Cake.bakery_offer[0], path=fr'/home/darek/Projects/to_task_102/'
                                                      fr'{Cake.export_1_cake_to_html.__name__}')
print('-' * 60)

# Here we are exporting the list of all cakes in our bakery to the html file using a class method.
Cake.export_all_cake_to_html_class = types.MethodType(export_all_cake_to_html_class, Cake)
Cake.export_all_cake_to_html_class(path=fr'/home/darek/Projects/to_task_102/'
                                        fr'{Cake.export_all_cake_to_html_class.__name__}')
print('-' * 60)
# Here we are exporting the list of all cakes in our bakery to the html file using a class instance.
Cake.export_all_cake_to_html_instance = types.MethodType(export_all_cake_to_html_instance, Cake)
# cake_01.export_all_cake_to_html_instance(path=fr'/home/darek/Projects/to_task_102/'
#                                               fr'{cake_01.export_all_cake_to_html_instance.__name__}')
# Here we are exporting to different folder separate html files include the name of cakes in its file name
for c in Cake.bakery_offer:
    c.export_all_cake_to_html_instance(path=fr"/home/darek/Projects/to_task_102/last/{c.name.replace(' ', '_')}")

print("Today's offer is:")
for number, elem in enumerate(Cake.bakery_offer):
    print('*' * 70)
    print(f'Number:{number + 1}')
    elem.show_info()
