import datetime

day_type = 3

weekend = 1
workday = 2
holiday = 3

if day_type == 1:
    pass

elif day_type == 2:
    pass

else:
    pass

day_description = 'weekend' if day_type == 1 else 'workday' if day_type == 2 else 'holiday'
print(day_description)

print('weekend') if day_type == 1 else print('workday') if day_type == 2 else print('holiday')
print('-------------------------------------------------------------------')

# Lab

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)
print('-------------------')

price = 123

print(price - bonus) if bonus_granted else print(price)
print('-------------------------------------------------------------------')

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
print('-------------------')

print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
print('-------------------------------------------------------------------')

today_weekday = datetime.date.today().strftime('%A')

mon = "On Monday I can't because, I am helping my mother"
tue_wed = 'On Tuesday and Wednesday you got to do washing'
thu = 'On Thursday I have got duty'
fri = 'On Friday I have two gatherings'
sat = 'On Saturday you cannot because you having lessons'
sun = 'But Sunday will be for us'

if today_weekday == 'Monday':
    print(mon)

elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print(tue_wed)

elif today_weekday == 'Thursday':
    print(thu)

elif today_weekday == 'Friday':
    print(fri)

elif today_weekday == 'Saturday':
    print(sat)

else:
    print(sun)
print('-------------------')

print(mon) if today_weekday == 'Monday' else print(tue_wed) if today_weekday == 'Tuesday' or \
                                                               today_weekday == 'Wednesday' \
    else print(thu) if today_weekday == 'Thursday' else print(fri) if today_weekday == 'Friday' \
    else print(sat) if today_weekday == 'Saturday' else print(sun)
