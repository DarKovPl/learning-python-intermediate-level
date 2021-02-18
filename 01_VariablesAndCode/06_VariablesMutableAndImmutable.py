number = 10
print('Variable number: ', number, id(number))
number += 2
print('Variable number: ', number, id(number))
print('-------------------------------------------------------------------')

text = 'Africa'
print('Variable text: ', text, id(text))
text += ' is hot'
print('Variable text: ', text, id(text))
print('-------------------------------------------------------------------')

list = [1, 2, 3]
print('Variable list: ', list, id(list))
list.append(4)
print('Variable list: ', list, id(list))
print('-------------------------------------------------------------------')

list_2 = list
print('Variable list_2', list_2, id(list_2))
list_2.append(5)
print('-----------------')
print('Variable list: ', list, id(list))
print('-----------------')
print('Variable list_2', list_2, id(list_2))
print('-------------------------------------------------------------------')

list_3 = list.copy()
print('Variable list: ', list, id(list))
print('-----------------')
print('Variable list_3', list_3, id(list_3))
print('-----------------')
list_3.append(6)
print('Variable list: ', list, id(list))
print('-----------------')
print('Variable list_3', list_3, id(list_3))
print('-------------------------------------------------------------------')

#  Laboratory

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
work_days = days.copy()
print('Variable days: {0:s} and\nVariable work_days: {1:s}.'.format(str(days), str(work_days)))
print('Id days: {0:d} and\nId work_days: {1:d}'.format(id(days), id(work_days)))
print('-----------------')
work_days.remove('sat')
work_days.remove('sun')
print('Variable days: {0:s} and\nVariable work_days: {1:s}.'.format(str(days), str(work_days)))
print('Id days: {0:d} and\nId work_days: {1:d}'.format(id(days), id(work_days)))
