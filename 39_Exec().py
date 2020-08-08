import os

# var_x = 10
#
# source = 'var_x = 12'
#
# result = exec(source)
# print(result)
# print('-----------')
#
# print(var_x)
# print('-------------------------------------------------------------------')
#
# source = '''
# new_var = 1
# for i in range(var_x):
#     print('-*' * i)
#     new_var += i
# '''
#
# result = exec(source)
# print(result)
# print('-----------')
#
# print(var_x)
# print(new_var)
#
# source = input('Enter your expression: ')
# print(eval(source))
# print('-------------------------------------------------------------------')

# Lab

files_to_process = [
    r"/tmp/math_sin_square.py",
    r"/tmp/math_square_root.py"
    ]

if not os.path.isfile(files_to_process[0]):

    with open(files_to_process[0], 'w') as file:
        code_to_write = '''
import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))
'''
        file.write(code_to_write)

if not os.path.isfile(files_to_process[1]):

    with open(files_to_process[1], 'w') as file:
        code_to_write = '''
import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(x**3 - x**0.5))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))
'''
        file.write(code_to_write)

print(os.path.basename(files_to_process[0]) + '\n' + os.path.basename(files_to_process[1]))

with open(files_to_process[0], 'r') as source, open(files_to_process[1], 'r') as source_1:

    print(exec(source.read()))
    print(exec(source_1.read()))
