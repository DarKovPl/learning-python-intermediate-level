work_days = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

month_days = dict(zip(months, work_days))
print(month_days)
print('-----------')

for key in month_days:
    print('Months: {} and workdays: {}'.format(key, month_days[key]))
print('-----------')

for val in month_days.values():
    print('Only values: {}'.format(val))
print('-----------')

for key in month_days.keys():
    print('Only keys: {}'.format(key))
print('-------------------------------------------------------------------')

# Lab

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

if len(dict_denominations) <= 0:

    for item in banknotes_coins:
        dict_denominations.update({item: 0})

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for mon, amount in dict_denominations.items():
    print('Denominate: %6.2f - amount: %5d' % (mon, amount))
