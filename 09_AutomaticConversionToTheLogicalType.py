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
