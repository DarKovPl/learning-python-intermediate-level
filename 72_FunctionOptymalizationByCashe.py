import time
import functools


#
#
# @functools.lru_cache()
# def factorial(n):
#     time.sleep(0.1)
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# start = time.time()
# for i in range(1, 11):
#     print(f'{i}! = {factorial(i)}')
# stop = time.time()
#
# print('Execution time', stop - start)
# print(factorial.cache_info())
#
#
# '''start = time.time()
# for i in range(1, 11):
#     print(f'{i}! = {factorial(i)}')
# stop = time.time()
#
# print('Execution time', stop - start)'''

#  Lab

def time_counting_function(func):
    def _counting_fib(*args):
        start = time.time()
        fib_result = func(*args)
        print('------', args)
        for i in args:
            stop = time.time()
            time_result = stop - start
            print(f'Fibonacci word: {i} and the number: {fib_result}. '
                  f'Work time {time_result}')
        return fib_result

    return _counting_fib


@time_counting_function
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

fib(6)