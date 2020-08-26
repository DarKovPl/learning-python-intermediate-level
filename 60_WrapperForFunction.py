import datetime
import functools


def change_salary(emp_name, new_salary, is_bonus=False):
    print("Changing salary for {} to {} as bonus={}".format(emp_name,
                                                            new_salary,
                                                            is_bonus))
    return new_salary


print(change_salary('Johnson', 20000, True))
print('--------------')


def create_function_with_wrapper(func):
    def _func_with_wrapper(*args, **kwargs):
        print("Function '{}' started at {}".format(func.__name__,
                                                   datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return _func_with_wrapper


change_salary_with_log = create_function_with_wrapper(change_salary)

print(change_salary_with_log('Johnson', 30000, is_bonus=True))
print('-------------------------------------------------------------------')

#       Second way:

change_salary = create_function_with_wrapper(change_salary)

print(change_salary('Johnson', 30000, is_bonus=True))
print('-------------------------------------------------------------------')


#       Third way

def create_function_with_wrapper(func):
    def _func_with_wrapper(*args, **kwargs):
        print("Function '{}' started at {}".format(func.__name__,
                                                   datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result

    return _func_with_wrapper


@create_function_with_wrapper
def change_salary(emp_name, new_salary, is_bonus=False):
    print("Changing salary for {} to {} as bonus={}".format(emp_name,
                                                            new_salary,
                                                            is_bonus))
    return new_salary


print(change_salary('Betty', 45000, is_bonus=True))
