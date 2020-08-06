# list_A = list(range(6))
# list_B = list(range(6))
#
# print(list_A, list_B)
# print('-----------')
#
# product = []
#
# for a in list_A:
#     for b in list_B:
#         product.append((a, b))
# print(product)
# print('-------------------------------------------------------------------')
#
# product = [(a, b) for a in list_A for b in list_B]
# print(product)
# print('-------------------------------------------------------------------')
#
# product = [(a, b) for a in list_A if a % 2 == 1 for b in list_B if b % 2 == 0]
# print(product)
# print('-------------------------------------------------------------------')
#
# product = {a: b for a in list_A if a % 2 == 1 for b in list_B if b % 2 == 0}
# print(product)
# print('-------------------------------------------------------------------')

# Lab

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flight = [(start, stop) for start in ports for stop in ports]
print(flight)
print(len(flight))
print('-----------')

flight_2 = [(start, stop) for start in ports for stop in ports if start != stop]
print(flight_2)
print(len(flight_2))
print('-----------')

flight_3 = [(start, stop) for start in ports for stop in ports if start > stop]
print(flight_3)
print(len(flight_3))

