# import datetime as dt
# import sys
#
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

