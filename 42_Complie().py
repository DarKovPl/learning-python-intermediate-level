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

str_formulas_lists = '''formulas_list += ["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)"]'''


if not os.path.isfile(r"/tmp/formulas_list"):
    with open(path_to_formulas, 'w') as file:
        file.write(str_formulas_lists)


with open(path_to_formulas, 'r') as f:
    formulas_list = []
    exec(f.read())

time_with_compile = time.time()
for item in formulas_list:
    print('Currently formula is executing: {}'.format(item))

    argument_list = []
    for i in range(1000000):
        argument_list.append(i / 10)

    result_list = []
    compiled_formula = compile(item, '/tmp/formulas_list', 'eval')
    for x in argument_list:
        result_list.append(eval(compiled_formula))

    print('Min value: {}'.format(min(result_list)), 'Max value: {}'.format(max(result_list)))

end_time = time.time()
print('Process time with compiled code: {}'.format(round(end_time - time_with_compile, 3)))
print('-------------------------------------------------------------------')

time_with_compile = time.time()
for item in formulas_list:
    print('Currently formula is executing: {}'.format(item))

    argument_list = []
    for i in range(1000000):
        argument_list.append(i / 10)

    result_list = []

    for x in argument_list:
        result_list.append(eval(item))

    print('Min value: {}'.format(min(result_list)), 'Max value: {}'.format(max(result_list)))

end_time = time.time()
print('Process time WITHOUT compiled code: {}'.format(round(end_time - time_with_compile, 3)))
