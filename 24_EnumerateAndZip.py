work_days = [19, 21, 22, 21, 20, 22]
print(work_days)
print('-----------')

enumerated_days = list(enumerate(work_days))
print(enumerated_days)
print('-----------')

for pos, value in enumerated_days:
    print('Position: {}'.format(pos), 'Value: {}'.format(value))
print('-------------------------------------------------------------------')

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

month_days = list(zip(months, work_days))
print(month_days)
print('-----------')

for m, d in zip(months, work_days):
    print('Month: ', m, 'Work days: ', d)
print('-----------')

for pos, (m, d) in enumerate(zip(months, work_days)):
    print('Position: {}, Month: {}\t and sum of workdays: {}'.format(pos, m, d))
print('-------------------------------------------------------------------')

#  Lab

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects, leaders):
    print('The leader of {} is {}.'.format(p, l))
print('-----------')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for pos, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print('{} -The leader of {} started {} is {}'.format(pos+1, p, d, l))
