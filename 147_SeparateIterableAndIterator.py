# import datetime as dt
#
#
# class MillionDaysIterator:
#     def __init__(self, date, max):
#         self.date = date
#         self.max_days = max
#
#     def __next__(self):
#         if self.max_days <= 0:
#             raise StopIteration()
#         ret = self.date
#         self.date += dt.timedelta(days=1)
#         self.max_days -= 1
#         return ret
#
#
# class MillionDays:
#     def __init__(self, year, month, day, max_days):
#         self.date = dt.date(year, month, day)
#         self.max_days = max_days
#         self.iterator = MillionDaysIterator(self.date, self.max_days)
#
#     def __iter__(self):
#         return self.iterator
#
#
# md = MillionDays(2000, 1, 1, 7)
# print(next(iter(md)))
# print('--------------------------------------')
#
# for d in md:
#     print(d)


# Lab
class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.iterator = CombinationsIterator(self.products, self.promotions, self.customers)

    def __iter__(self):
        return self.iterator


class CombinationsIterator:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration

        item_to_return = self.products[self.current_product], \
                         self.promotions[self.current_promotion], \
                         self.customers[self.current_customer]
        self.current_customer += 1
        return item_to_return


products = [f'Product {i}' for i in range(1, 4)]

promotions = [f'Promotion {i}' for i in range(1, 3)]

customers = [f'Customer {i}' for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

list_ = []
for c in combinations:
    list_.append(c)

print(list_[0])
print(len(list_))
