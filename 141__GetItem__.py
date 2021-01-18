import datetime as dt


class MillionDays:
    def __init__(self, year, month, day, max_days):
        self.date = dt.datetime(year, month, day)
        self.max_days = max_days

    def __getitem__(self, item):
        if item <= self.max_days:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration


md = MillionDays(2000, 1, 1, 20)

# print(md[0], md[1], md[2])

# print(next(md))
# print(next(md))
# print(next(md))

it = iter(md)

print(next(it))
print(next(it))
print(next(it))

for d in md:
    print(d)

# Lab

