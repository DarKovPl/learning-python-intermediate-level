import datetime
import functools

# log_file_patch = r'/tmp/function_log.txt'
#
#
# def create_function_with_wrapper(func):
#     def _func_with_wrapper(*args, **kwargs):
#         file = open(log_file_patch, 'a')
#         file.write('-' * 20 + '\n')
#         file.write(f'Function "{func.__name__}" started at: '
#                    f'{datetime.datetime.now().isoformat()}')
#         file.write('Following argument were used:\n')
#         file.write(' '.join(f"{x}" for x in args))
#         file.write("\n")
#         file.write(' '.join(f"{k}={v}" for k, v in kwargs.items()))
#         file.write("\n")
#         result = func(*args, **kwargs)
#         file.write(f'Function returned {result}\n')
#         file.close()
#
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
# print(change_salary('Betty', 45000, True))
# print(change_salary('Betty', 45000, is_bonus=True))
print('-------------------------------------------------------------------')


def create_function_with_wrapper_log_to_file(log_file_patch):
    def create_function_with_wrapper(func):
        def _func_with_wrapper(*args, **kwargs):
            file = open(log_file_patch, 'a')
            file.write('-' * 20 + '\n')
            file.write(f'Function "{func.__name__}" started at: '
                       f'{datetime.datetime.now().isoformat()}')
            file.write('Following argument were used:\n')
            file.write(' '.join(f"{x}" for x in args))
            file.write("\n")
            file.write(' '.join(f"{k}={v}" for k, v in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write(f'Function returned {result}\n')
            file.close()

            return result

        return _func_with_wrapper

    return create_function_with_wrapper


@create_function_with_wrapper_log_to_file(r'/tmp/change_salary_log.txt')
def change_salary(emp_name, new_salary, is_bonus=False):
    print("Changing salary for {} to {} as bonus={}".format(emp_name,
                                                            new_salary,
                                                            is_bonus))
    return new_salary


@create_function_with_wrapper_log_to_file(r'/tmp/change_position_log.txt')
def change_position(emp_name, new_position):
    print("Changing position for {} to {}.".format(emp_name, new_position))

    return new_position


print(change_salary('Betty', 45000, True))
print(change_salary('Betty', 45000, is_bonus=True))
print(change_position('Anke', 'Manager'))
print(change_position('Michael', 'Salesman'))
