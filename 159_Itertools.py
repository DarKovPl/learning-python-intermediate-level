import itertools as it
import math

# my_list = ['a', 'b', 'c', 'd']
#
# for combinations in it.combinations(my_list, 3):
#     print(combinations)
# print('------------------------------------------------------')
#
# for combinations in it.permutations(my_list, 3):
#     print(combinations)
# print('------------------------------------------------------')
#
# for combinations in it.combinations_with_replacement(my_list, 3):
#     print(combinations)
# print('------------------------------------------------------')
#
# money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
#
# results = []
#
# for i in range(1, 101):
#     for combinations in it.combinations(money, i):
#         if sum(combinations) == 100:
#             results.append(combinations)
#
# res = set(results)
#
# for i in res:
#     print(i)
# print('------------------------------------------------------')
#
# money = [50, 20, 10, 5, 1]
#
# for i in range(1, 101):
#     for combinations in it.combinations_with_replacement(money, i):
#         if sum(combinations) == 100:
#             print(combinations)

# Lab

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

perm = [note for note in it.permutations(notes, 4)]

comb = [note for note in it.product(notes, notes, notes, notes)]

factorial = lambda num: 1 if num <= 1 else num * factorial(num - 1)

# power = lambda num: num **

# def check_and_answer(list_of_elements, comb_of_perm, comb_of_, factorial, ):
#
#
#     if len(list_of_elements) ==
