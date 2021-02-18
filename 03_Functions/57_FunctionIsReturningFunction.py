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

# # Lab
units = {'minutes': 60, 'hours': 3600, 'days': 86400}


def main_function(enter_date):
    """This function is able to count time between two dates. One date is got from the user,
    and the second date is a current date. Function is able to return the counted result as one
    of three units of time chosen by the user """

    f_time_variable = """
from dateutil import parser
from datetime import datetime


def f_time(units_of_time, input_date=parser.parse('{}'),
           current_time=datetime.now()):

    result = current_time - input_date
    seconds = result.total_seconds()
    output =  round(round(seconds, 0) / int(units_of_time), 0)

    return output
""".format(enter_date)

    exec(f_time_variable, globals())

    return f_time


input_date_to_main = input("Please enter here the date 'RRRR-MM-DD HHMMSS': ")
choose_unit = input('Please choose which unit of the time you want to work?\n{}\nEnter chosen value here-->'
                    ''.format('\n'.join(unit + '-' + str(val) for unit, val in units.items())))


rt = main_function(enter_date=input_date_to_main)
print(rt(units_of_time=choose_unit))

print('-------------------------------------------------------------------')
# and here we have printed all three units of time because the author of
# the lab has included that in his answer.
for i in units.values():
    print(rt(units_of_time=i))
