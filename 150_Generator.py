# import datetime as dt
#
#
# def million_days(year, month, day, max_days):
#     date = dt.date(year, month, day)
#     for i in range(max_days):
#         yield date + dt.timedelta(days=i)
#
#
# for d in million_days(2000, 1, 1, 3):
#     print(d)
#
#
# def get_magic_numbers():
#     yield 22
#     yield 4
#     yield 5


# r = get_magic_numbers()
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# for i in get_magic_numbers():
#     print(i)


# Lab

def combinations():
    for p in [f'Product {i}' for i in range(1, 4)]:
        for prom in [f'Promotion {i}' for i in range(1, 3)]:
            for c in [f'Customer {i}' for i in range(1, 5)]:
                yield p, prom, c


z = []
for i in combinations():
    print(i)
    z.append(i)
print(len(z))
