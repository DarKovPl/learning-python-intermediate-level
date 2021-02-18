# def double(x):
#     return x * 2
#
#
# x = 10
# x = double(x)
# print(x)
#
# z = 10
# f = lambda x: x * 2
# print(f(z))
# print('-------------------------------------------------------------------')
#
#
# def power(x, y):
#     return x ** y
#
#
# x = 5
# y = 3
# print(power(x, y))
#
# f = lambda x, y: x ** y
# print(f(x, y))
# print('-------------------------------------------------------------------')
#
# list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]
#
#
# def is_odd(x):
#     return x % 2 != 0
#
#
# print(is_odd(7), is_odd(4))
#
# filtered_list = list(filter(is_odd, list_numbers))
# print(filtered_list)
#
# filtered_list = list(filter(lambda x: x % 2 != 0, list_numbers))
# print(filtered_list)
# print('-------------------------------------------------------------------')
#
# print(list(filter(lambda x: x % 2 != 0, list_numbers)))
# print('-------------------------------------------------------------------')


def generate_multiply_function(n):
    return lambda x: n * x


mul_2 = generate_multiply_function(2)
mul_3 = generate_multiply_function(3)

print(mul_2(13), mul_3(8))
print('-------------------------------------------------------------------')

# Lab

text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']
text = 'oddd'

f = lambda s: print(len(s))

f(text)
print('-------------------------------------------------------------------')

list(map(f, text_list))
print('-------------------------------------------------------------------')

print(list(map(lambda f: len(f), text_list)))
