is_ok = True
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = 'True'
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = ''
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = 1
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = 0
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = -1
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = [1, 2, 3]
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = []
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = [0, 0, 0]
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok:
    print('TRUE')
print('-------------------------------------------------------------------')

is_ok = [0, 0, 0]
print("Variable is_ok: ", is_ok, type(is_ok))
if is_ok[0]:  # reference to a list item zero
    print('TRUE')
print('-------------------------------------------------------------------')

list_of_errors = [100, 101, 102]
print("Variable list_of_errors: ", list_of_errors, type(list_of_errors))
if list_of_errors:
    print('TRUE')
print('-------------------------------------------------------------------')

list_of_errors = [100, 101, 102]
print("Variable list_of_errors: ", list_of_errors, type(list_of_errors))
if len(list_of_errors) > 0:
    print('TRUE')
print('-------------------------------------------------------------------')

# Lab

option_list = [' load data', ' export data', ' analyze & predict']
chosen_option = 0


while not chosen_option:

    try:
        chosen_option = int(input('Please choose one of the options: \n{}.\nEnter the number of your choice here -->'
                                  .format('\n'.join(str(num + 1) + elem
                                                    for num, elem in zip(range(len(option_list)), option_list)))))
        if 0 < chosen_option <= 3:
            print('You chosen: {0:d}{1:s}'.format(chosen_option, option_list[chosen_option - 1]))

        else:
            print('Your entered value is above the range: %d' % chosen_option if chosen_option > 3
                  else 'Your entered value is below the range: %d' % chosen_option)
            chosen_option = 0

    except ValueError as e:
        print("\nThis error has occurred: '%s'" % e, 'Please enter the correct int value.')
