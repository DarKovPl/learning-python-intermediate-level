import csv

# print('Tuple:')
# a_tuple = (1, 2, 3, 4, 5)
#
# for x in a_tuple:
#     print(x)

# print(next(a_tuple))  #  tuple is without an iterator
# print('---------------------------')
# it = iter(a_tuple)
# print(next(it))
# print(next(it))
# print(next(it))
# print('------------------------------------------------------------------')
#
# print('List:')
# a_list = [1, 2, 3, 4, 5]
#
# for i in a_list:
#     print(i)

# print(next(a_list))   #  list is without an iterator
# print('------------------------------------------------------------------')

# print('Set:')
# a_set = {1, 2, (3, 4), 'another element', 3, 4}
#
# for i in a_set:
#     print(i)

# print(next(a_set)) # set is without an iterator
# print('------------------------------------------------------------------')
# print('Reading from file:')
# file is iterable and it has its own iterator

# # with open('/home/darek/Projects/to_task_144/lines.txt', 'r') as file:
# #   for line in file:
# #      print(line)

# with open('/home/darek/Projects/to_task_144/lines.txt', 'r') as file:
#     while True:
#         try:
#             print(next(file))
#         except StopIteration:
#             break
# Lab

with open('/home/darek/Projects/to_task_145/data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # for row in csv_reader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csv_reader))
        except StopIteration:
            break
