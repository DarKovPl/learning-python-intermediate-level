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
units = {'minutes': 60, 'hours': 3600, 'days': 86400}


def main_function(enter_date=input("Please enter here the date 'RRRR-MM-DD HH MM SS': "),
                  units_of_time=input('Please chose which unit of date you want to work?\n{}\n'
                                      'Enter chosen value here-->'
                                      ''.format('\n'.join(unit + '-' + str(val) for unit, val in units.items())))):
    f_minutes_variable = """
from dateutil import parser
from datetime import datetime


def f_time(input_date=parser.parse(str({})),
           current_time=datetime.now(), unit={}):

    result = current_time - input_date
    seconds = result.total_seconds()
    output =  round(round(seconds, 0) / unit, 0)

    return output
""".format(enter_date, units_of_time)
    exec(f_minutes_variable, globals())

    return f_time()


print(main_function())

