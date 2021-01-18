import datetime as dt
import sys
import time


# start = dt.datetime.now()
# print(f'Execution started at: {start}')


# dates = [dt.date(2000, 1, 1) + dt.timedelta(days=i) for i in range(2500000)]
# print(f'size of dates is {sys.getsizeof(dates)}')
# for d in dates:
#     pass


# class MillionDays:
#     def __init__(self, year, month, day, max_days):
#         self.date = dt.date(year, month, day)
#         self.max_days = max_days
#
#     def __next__(self):
#
#         if self.max_days <= 0:
#             raise StopIteration()
#         ret = self.date
#         self.date += dt.timedelta(days=1)
#         self.max_days -= 1
#         return ret
#
#     def __iter__(self):
#         return self
#
#
# md = MillionDays(2000, 1, 1, 2500000)
# print(f'size of dates is {sys.getsizeof(md)}')
# for d in md:
#     pass

# md = MillionDays(2000, 1, 1, 2500000)
# print(f'size of dates is {sys.getsizeof(md)}')
# # print(next(md))
# # print(next(md))
# # print(next(md))
#
# for i in range(2500000):
#     next(md)

# stop = dt.datetime.now()
# print(f'Execution started at: {stop}')
# print(f'Total time: {stop - start}')

# Lab


class Combinations:

    def __init__(self, products, promotions, customers,
                 current_product=0, current_promotion=0, current_customer=0):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = current_product
        self.current_promotion = current_promotion
        self.current_customer = current_customer

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

    def __iter__(self):
        return self


products = [f'Product {i}' for i in range(1, 500)]

promotions = [f'Promotion {i}' for i in range(1, 50)]

customers = [f'Customer {i}' for i in range(1, 500)]

combinations = Combinations(products, promotions, customers)

list_ = []
for c in combinations:

    list_.append(c)


print(list_[0])
print(len(list_))
