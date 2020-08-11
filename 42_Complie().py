import time
import math
import os

# source = 'report_line += 1'
#
# report_line = 0
#
# start = time.time()
# for i in range(100000):
#     exec(source)
# stop = time.time()
# time_not_compiled = stop - start
# print(time_not_compiled)
# print('-----------')
#
# start = time.time()
# source_compiled = compile(source, 'internal variable source', 'exec')
# for i in range(100000):
#     exec(source_compiled)
# stop = time.time()
# time_compiled = stop - start
# print(time_compiled)
# print('-----------')
#
# print(time_not_compiled / time_compiled)
# print('-----------')
#
# print(report_line)
print('-------------------------------------------------------------------')

# Lab

path_to_formulas = r"/tmp/formulas_list"

str_formulas_lists = '''formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]'''

if not os.path.isfile(r"/tmp/formulas_list"):
    with open(path_to_formulas, 'w') as file:
        file.write(str_formulas_lists)

with open(path_to_formulas, 'r') as f:
    imported_formulas_from_file = f.readlines()
    zebra = imported_formulas_from_file.pop(1)[:-2].lstrip()

    to_string = ''.join(g for g in zebra)

    argument_list = []
    for i in range(1000000):
        argument_list.append(i / 10)

    for divided in argument_list:
        to_almost_compiling = to_string.replace('x', str(divided))

compiled_formulas_list = compile(to_almost_compiling, r'/tmp/formulas_list', 'eval')
print(eval(compiled_formulas_list))
