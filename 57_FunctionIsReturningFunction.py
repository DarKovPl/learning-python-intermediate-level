import time


def calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for a in args:
            result += 1
    elif kind == '-':
        for a in args:
            result -= a
    return result


print(calculate('+', 1, 2, 3))
print(calculate('-', 1, 2, 3))
print('-------------------------------------------------------------------')


def create_function(kind='+'):
    source = """
def f(*args):
   result = 0
   for a in args:
       result {}= a
   return result
""".format(kind)
    exec(source, globals())

    return f


f_add = create_function('+')
print(f_add(1, 2, 3, 4))

f_sub = create_function('-')
print(f_sub(10, 20, 30))
print('-------------------------------------------------------------------')

# Lab

# def main_function(date):
#     f_minutes_variable = ''''''
from datetime import datetime


def f_minutes(input_date=(2020, 10, 10),
              time=datetime.now()):
    z = datetime.(input_date)
    result = z - time

    return print(result)


f_minutes()
