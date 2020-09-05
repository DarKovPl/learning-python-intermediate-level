import datetime
import functools
import time

# def change_salary(emp_name, new_salary, is_bonus=False):
#     print("Changing salary for {} to {} as bonus={}".format(emp_name,
#                                                             new_salary,
#                                                             is_bonus))
#     return new_salary
#
#
# print(change_salary('Johnson', 20000, True))
# print('--------------')
#
#
# def create_function_with_wrapper(func):
#     def _func_with_wrapper(*args, **kwargs):
#         print("Function '{}' started at {}".format(func.__name__,
#                                                    datetime.datetime.now().isoformat()))
#         print('Following arguments were used:')
#         print(args, kwargs)
#         result = func(*args, **kwargs)
#         print('Function returned {}'.format(result))
#         return result
#
#     return _func_with_wrapper
#
#
# change_salary_with_log = create_function_with_wrapper(change_salary)
#
# print(change_salary_with_log('Johnson', 30000, is_bonus=True))
# print('-------------------------------------------------------------------')
#
# #       Second way:
# print('Second way\n')
#
# change_salary = create_function_with_wrapper(change_salary)
#
# print(change_salary('Johnson', 30000, is_bonus=True))
# print('-------------------------------------------------------------------')
#
# #       Third way
# print('Third way\n')
#
#
# def create_function_with_wrapper(func):
#     def _func_with_wrapper(*args, **kwargs):
#         print("Function '{}' started at {}".format(func.__name__,
#                                                    datetime.datetime.now().isoformat()))
#         print('Following arguments were used:')
#         print(args, kwargs)
#         result = func(*args, **kwargs)
#         print('Function returned {}'.format(result))
#         return result
#
#     return _func_with_wrapper
#
#
# @create_function_with_wrapper
# def change_salary(emp_name, new_salary, is_bonus=False):
#     print("Changing salary for {} to {} as bonus={}".format(emp_name,
#                                                             new_salary,
#                                                             is_bonus))
#     return new_salary
#
#
# print(change_salary('Betty', 45000, is_bonus=True))

#  Lab


def get_sequence_wrapper(function):
    def _wrapped_function(*args):

        time_start = time.time()
        result = function(*args)
        time_stop = time.time()

        print(f'Function name: "{function.__name__}" and time of its work:'
              f' {time_stop - time_start}')

        return result
    return _wrapped_function


@get_sequence_wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(14))
