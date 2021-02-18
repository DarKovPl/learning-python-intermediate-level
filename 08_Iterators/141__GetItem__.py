import datetime as dt


# class MillionDays:
#     def __init__(self, year, month, day, max_days):
#         self.date = dt.datetime(year, month, day)
#         self.max_days = max_days
#
#     def __getitem__(self, item):
#         if item <= self.max_days:
#             return self.date + dt.timedelta(days=item)
#         else:
#             raise StopIteration
#
#
# md = MillionDays(2000, 1, 1, 20)

# print(md[0], md[1], md[2])

# print(next(md))
# print(next(md))
# print(next(md))

# it = iter(md)
#
# print(next(it))
# print(next(it))
# print(next(it))
#
# for d in md:
#     print(d)

# Lab

class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= (len(self.products) * len(self.promotions) * len(self.customers)):
            raise StopIteration
        else:
            pos_products = item % (len(self.promotions) * len(self.customers)) == 0
            item = pos_products

            pos_promotions = item % len(self.customers) == 0
            item = pos_promotions

            pos_customers = item

            print_string = products[pos_products], promotions[pos_promotions], customers[pos_customers]

        return print_string


products = [f'Product {i}' for i in range(1, 4)]

promotions = [f'Promotion {i}' for i in range(1, 3)]

customers = [f'Customer {i}' for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

z = []
# for i in range(30):
#     print(combinations[i])
#     z.append(combinations[i])
# print(len(z))
# print(z)

it = iter(combinations)

# print(next(it))
# print(next(it))

for i in it:
    z.append(i)
    print(i)

print(len(z))
