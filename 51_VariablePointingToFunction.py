# def buy_me(what):
#     print('Give me', what)
#
#
# buy_me('a new car.')
# print('-------------------------------------------------------------------')
#
# steal_for_me = buy_me
# print(type(steal_for_me))
#
# steal_for_me('a new car')
# print('-------------------------------------------------------------------')
#
#
# def go_left(*args):
#     print('PLACEHOLDER - turning left with', *args)
#
#
# def go_right(*args):
#     print('PLACEHOLDER - turning right with', *args)
#
#
# def go_forward(*args):
#     print('PLACEHOLDER - going forward with', *args)
#
#
# def go_back(*args):
#     print('PLACEHOLDER - going back with', *args)
#
#
# def start(*args):
#     print('PLACEHOLDER - starting with', *args)
#
#
# def stop(*args):
#     print('PLACEHOLDER - stopping with', *args)
#
#
# dish = 'pizza'
# instructions = [start, go_forward, go_forward, go_left, go_forward, go_right, stop]
#
# for instr in instructions:
#     instr(dish)
print('-------------------------------------------------------------------')


# Lab

def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x/2


number = 8
transformations = [double, root, div2, negative]
transformations_1 = [root, root, div2, double]

print('Operation starts here')
tmp_return_value = number
for action in transformations:
    tmp_return_value = action(tmp_return_value)
    print(tmp_return_value)
print('First operation is ending here')
print('--------------')

print('Second operation started here')
tmp_return_value = number
for action_1 in transformations_1:
    tmp_return_value = action_1(tmp_return_value)
    print(tmp_return_value)
print('All operations have been ended.')
