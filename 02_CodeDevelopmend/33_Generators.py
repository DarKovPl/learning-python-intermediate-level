# list_A = list(range(6))
# list_B = list(range(6))
#
# product = [(a, b) for a in list_A if a % 2 == 1 for b in list_B if b % 2 == 0]
# print(product)
# print('-----------')
#
# gen = ((a, b) for a in list_A if a % 2 == 1 for b in list_B if b % 2 == 0)
# print(gen)
# print('-----------')
#
# print(next(gen))
# print(next(gen))
# print('-----------')
#
# for x in gen:
#     print(x)
# print('-----------')
#
# gen = ((a, b) for a in list_A if a % 2 == 1 for b in list_B if b % 2 == 0)
#
# while True:
#
#     try:
#         print(next(gen))
#
#     except StopIteration:
#         print('Printing the list has been ended')
#         break
print('-------------------------------------------------------------------')

# Lab

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen = ((start, stop) for start in ports for stop in ports)
print(gen)
print('-----------')
sum = 0

for item in gen:
    sum += 1
    print(item)
print(sum)
print('-------------------------------------------------------------------')

gen = ((start, stop) for start in ports for stop in ports if start != stop)
print(gen)
print('-----------')

sum = 0

for item in gen:
    sum += 1
    print(item)
print(sum)
print('-------------------------------------------------------------------')

gen = ((start, stop) for start in ports for stop in ports if start > stop)
print(gen)
print('-----------')

sum = 0

for item in gen:
    sum += 1
    print(item)
print(sum)
