import os


# def buy_me(prefix='Please buy me', what='something nice.', *args, **kwargs):
#     print(prefix, what)
#     print(args)
#     print(kwargs)
#
#
# buy_me('Please buy me', 'a new car.', 'a new car', 'a cat', 'a dog', 'a dragon',
#        shop='market', colour='any')
#
# products = ['milk', 'bread', 'cereal']
# parameters = {'price': 'low', 'time': 'now'}
#
# buy_me('Buy me', 'newspaper', *products, **parameters)

# Lab

def calculate_paint(efficiency_m2_per_ltr=4.2, *args):
    """this function is counting the quantity of paint needed to paint
       stated meters by the customer"""
    counter = 0
    total_paint = 0
    for room in args:
        needed_paint = room / efficiency_m2_per_ltr
        total_paint += needed_paint
        counter += 1
        print('Room %d needs:' % counter, round(needed_paint, 2))
    print('Total amount of paint: %.2f' % total_paint)


meters = [50, 75, 78]
calculate_paint(5.5, *meters)
print('-------------------------------------------------------------------')


def log_it(path_to_file=r'/tmp/log_it.txt', *args):
    str_command = args
    with open(path_to_file, 'a+') as file:
        for item in str_command:
            file.write(item + ' ')
        file.write('\n')
    print('To file was added these expressions: {}'.format(str_command))


log_it(r'/tmp/log_it.txt', 'ERROR', 'Not enough data', 'invoices', '2020')
log_it(r'/tmp/log_it.txt', 'Starting processing forecasting')
