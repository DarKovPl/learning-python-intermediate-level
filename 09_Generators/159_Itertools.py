import itertools as it
import functools

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

value_of_song_notes = 4  # Here you can change the number of song notes

var_without_rep = [note for note in it.permutations(notes, value_of_song_notes)]

var_with_rep = [note for note in it.product(notes, repeat=value_of_song_notes)]

factorial = lambda num: 1 if num <= 1 else num * factorial(num - 1)

power = lambda num, power: num ** power


def check_and_print(song_without_rep, song_with_rep, fact, pow, for_div):

    math_form = fact / for_div
    if (len(song_without_rep), len(song_with_rep)) == (math_form, pow):
        print(f'Amount of the variations WITHOUT repetition is correct, and the total is {int(math_form)}.',
              f'Amount of the variations WITH repetition is correct, and the total is {pow}')
    else:
        raise Exception('Something went wrong. Please check arguments')


to_factorial = functools.partial(factorial, len(notes))
to_power = functools.partial(power, len(notes), value_of_song_notes)
to_div = functools.partial(factorial, len(notes) - value_of_song_notes)
for_check_and_print = functools.partial(check_and_print, var_without_rep, var_with_rep)

for_check_and_print(to_factorial(), to_power(), to_div())
