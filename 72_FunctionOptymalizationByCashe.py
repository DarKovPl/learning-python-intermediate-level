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

@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


def range_loop(ran):
    tim_start = time.time()
    for i in range(ran):
        fib_result = fib(i)
        print(f'Fibonacci word: {i} and the number: {fib_result}. Work time {round(time.time() - tim_start, 4)}')


range_loop(11)
print(fib.cache_info())

range_loop(12)
print(fib.cache_info())
