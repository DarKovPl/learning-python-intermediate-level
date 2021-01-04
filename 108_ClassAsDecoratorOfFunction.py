import random


# class MemoryClass:
#     list_of_already_selected_items = []
#
#     def __init__(self, func):
#         print('>>> This is init of MemoryClass')
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('>>> This is call of MemoryClass instance')
#         items_not_selected = [i for i in args if i not in MemoryClass.list_of_already_selected_items]
#         print('+++ Selecting only from a list of', items_not_selected)
#         item = self.func(items_not_selected)
#         MemoryClass.list_of_already_selected_items.append(item)
#         return item
#
#
# cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot',
#         'Porsche', 'VW', 'Audi', 'Mazda']
#
#
# @MemoryClass
# def select_today_promotion(list_of_cars):
#     return random.choice(list_of_cars)
#
#
# @MemoryClass
# def select_today_show(list_of_cars):
#     return random.choice(list_of_cars)
#
#
# @MemoryClass
# def select_free_accessories(list_of_cars):
#     return random.choice(list_of_cars)
#
#
# print('Promotion:', select_today_promotion(*cars))
# print('Show:', select_today_show(*cars))
# print('Free accessories:', select_free_accessories(*cars))


# Lab

# My way to solve the problem
class NoDuplicates:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        additives_not_in_instance = [a for a in args[1:] if not a in args[0].additives]
        self.func(args[0], additives_not_in_instance)


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

    def add_additives(self, additives):
        self.additives.extend(additives)


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

cake_02 = Cake('Pear-Ginger Pie', 'Cake', 'Ginger',
               additives=['pears', 'crystallized ginger',
                          'orange juice', 'cinnamon'], filling='')

add_extra_additives(cake01, 'strawberries', 'sugar-flowers')
cake01.show_info()

add_extra_additives(cake01, 'strawberries', 'sugar-flowers', 'chocolate', 'nuts', 'mayo')
cake01.show_info()

add_extra_additives(cake_02, 'orange juice', 'cinnamon', 'chocolate', 'nuts')
cake_02.show_info()


#  Step by step, following the lab instructions
# class NoDuplicates:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, cake, additives):
#         no_duplicate_list = []
#         for i in additives:
#             if not i in cake01.additives:
#                 no_duplicate_list.append(i)
#         self.func(cake, no_duplicate_list)
#
#
# class Cake:
#     bakery_offer = []
#
#     def __init__(self, name, kind, taste, additives, filling):
#
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-' * 20)
#
#     def add_additives(self, additives):
#         self.additives.extend(additives)
#
#
# cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
#
#
# @NoDuplicates
# def add_extra_additives(cake, additives):
#     cake.add_additives(additives)
#
#
# add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
# cake01.show_info()
#
# add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolate', 'nuts', 'mayo'])
# cake01.show_info()
