def bake(what):
    print('Baking {}'.format(what))


def add(what):
    print('Adding {}'.format(what))


def mix(what):
    print('Mixing {}'.format(what))


cookbook = [(add, 'milk'), (add, 'eggs'), (add, 'flour'), (add, 'sugar'),
            (mix, 'ingredients'), (bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)
print('--------------')


def cook(activity, obj):
    activity(obj)


cook(bake, 'brownies')
print('--------------')

for activity, obj in cookbook:
    cook(activity, obj)
print('-------------------------------------------------------------------')

# Lab

x_table = list(range(11))


def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(function, ingredients):
    """This function is a common interface for the above functions, and it is able to send
     ingredients from x_table to every function and download the result of the calculation and print it"""

    for x_ing in ingredients:
        print("Function: '{}' and the result of calculation: {}".format(function.__name__, function(x_ing)))


generate_values(double, x_table)
generate_values(root, x_table)
generate_values(negative, x_table)
generate_values(div2, x_table)
