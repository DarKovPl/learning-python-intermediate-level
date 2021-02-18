# class MemoryClass:
#
#     def __init__(self, list):
#         self.list_of_items = list
#
#     def __call__(self, *args, **kwargs):
#         self.list_of_items.append(*args)
#
#
# mem = MemoryClass([])
# print('List of items in memory', mem.list_of_items)
#
# mem.list_of_items.append('buy sugar')
# print('List of items in memory', mem.list_of_items)
#
# print('This class is callable', callable(MemoryClass))
# print('This class is callable', callable(mem))
#
# mem('buy milk')
# print('List of items in memory', mem.list_of_items)
#
# mem('buy coffee')
# print('List of items in memory', mem.list_of_items)
#
# print('This class is callable', callable(MemoryClass))
# print('This class is callable', callable(mem))


# Lab

class NoDuplicates:

    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for elem in new_items:
            if not elem in self.list:
                self.list.append(elem)


my_no_dup_list = NoDuplicates()
my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)
