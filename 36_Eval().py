import math

var_x = 10
password = 'My super secret password'

source = 'var_x + 2'

result = eval(source)
print(result)
print('-------------------------------------------------------------------')

source = 'password'

result = eval(source)
print(result)
print('-------------------------------------------------------------------')

print(globals())

globals_copy = globals().copy()
del globals_copy['password']
print('-----------')

# source = 'password'
source = 'var_x + 3'

result = eval(source, globals_copy)
print(result)
print('-------------------------------------------------------------------')

globals_copy = {}

#  source = 'var_x + 3'
source = '33 + 3'

result = eval(source, globals_copy)
print(result)
print('-------------------------------------------------------------------')

source = "__import__('os').getcwd()"

result = eval(source, globals_copy)
print(result)
print('-------------------------------------------------------------------')


#  Lab

def list_of_arguments(argument=range(0, 100, 1)):
    argument_list = [(item / 10) for item in argument]
    return argument_list


def enter_the_formula():
    formula = input("Enter the formula with the x coefficient here: ")
    return str(formula.lower())


def counting_everything_together():
    argument_list = list_of_arguments()
    formula = enter_the_formula()

    try:

        for arg in argument_list:
            formula_after = formula.replace('x', str(arg), len(argument_list))
            print(eval(formula_after))

    except NameError:
        print('You entered the formula with the wrong character of'
              ' the alphabet as a coefficient.')


counting_everything_together()
print('-------------------------------------------------------------------')

# argument_list = []
#
# for i in range(100):
#     argument_list.append(i / 10)
#
# formula = input("Please enter a formula, use 'x' as the argument: ")
#
# for x in argument_list:
#     print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))
