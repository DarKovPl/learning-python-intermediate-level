import itertools
import operator

#  itertools.accumulate(iterable, func)
print(' 1- itertools.accumulate(iterable, func). With operator.mul')

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

#  itertools.accumulate(iterable, func)
print(' 2- itertools.accumulate(iterable, func). With max')

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, max)
for each in result:
    print(each)
print(' 3- itertools.accumulate(iterable, func). With max and 13 in the middle.')

data = [1, 2, 13, 4, 5]
result = itertools.accumulate(data, max)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.count(start=0, step=1)
print(' 4- itertools.count(start=0, step=1).')

for i in itertools.count(10, 3):
    print(i)
    if i > 20:
        break
print('---------------------------------------------------------------------------')

# itertools.cycle(iterable)
print(' 5- itertools.cycle(iterable). Endless loop is in comment')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# for m in itertools.cycle(months):
#     print(m)
print('---------------------------------------------------------------------------')

# itertools.chain(*iterables)
print(' 6- itertools.chain(*iterables).')

colors_basic = ['red', 'yellow', 'blue']
colors_mix = ['green', 'orange', 'violet']
result = itertools.chain(colors_basic, colors_mix)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.compress(data, selectors)
print(' 7- itertools.compress(data, selectors).')

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.dropwhile(predicate, iterable)
print(' 8- itertools.dropwhile(predicate, iterable).')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x < 5, data)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.filterfalse(predicate, iterable)
print(' 9- itertools.filterfalse(predicate, iterable).')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.filterfalse(lambda x: x < 5, data)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.islice(iterable, start, stop, step)
print(' 10- itertools.islice(iterable, start, stop, step).')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
result = itertools.islice(months, 6, 8)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.product(iterable, iterable)
print(' 11- itertools.product(iterable, iterable).')

spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
result = itertools.product(spades, figures)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.repeat(object, times)
print(' 12- itertools.repeat(object, times). Endless loop is in comment')

# for i in itertools.repeat('tell me more'):
#     print(i)

print(' 13- itertools.repeat(object, times). With "times" parameter.')
for i in itertools.repeat('tell me more', 5):
    print(i)
print('---------------------------------------------------------------------------')

# itertools.starmap(function, iterable)
print(' 14- itertools.starmap(function, iterable).')

data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(operator.add, data)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.takewhile(predicate, iterable)
print(' 15- itertools.takewhile(predicate, iterable).')

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x < 5, data)
for each in result:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.tee(iterable, n=2)
print(' 16- itertools.tee(iterable, n=2).')

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars_1, cars_2 = itertools.tee(cars)

for each in cars_1:
    print(each)
print('-----------------')

for each in cars_2:
    print(each)
print('---------------------------------------------------------------------------')

# itertools.zip_longest(*iterables, fillvalue=None)
print(' 17- itertools.zip_longest(*iterables, fillvalue=None).')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free', 'free']
result = itertools.zip_longest(months, plan, fillvalue='unknown')
for each in result:
    print(each)
print('---------------------------------------------------------------------------')


# Lab

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


candidate_list = [num for num in range(1, 1001)]
filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))
for num in filtered_list:
    print(num, get_factors(num))
print('---------------------------------------------------------------------------')


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False


# prime_numbers = list(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
# print(prime_numbers)
# print(prime_numbers[:10])
prime_numbers = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))