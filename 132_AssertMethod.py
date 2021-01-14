import datetime as dt

# net_value = 100
# gross_value = 120
# #  net_value must be less or equal to gross_value
# assert net_value <= gross_value, 'net_value cannot be greater than gross_value'
#
# order_date = dt.date(2022, 10, 13)
# delivery_date = dt.date(2022, 10, 18)
# #  order date should be earlier than the delivery date
# assert order_date <= delivery_date, 'Order date cannot be later than delivery date'


# Lab

class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):

        assert len(self.title) > 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"


    @classmethod
    def publish_offer(cls, tours):

        list_of_errors = []

        for tour in tours:

            try:
                tour.check_data()
            except ValueError as e:
                list_of_errors.append(f'{tour.symbol}; {e}')
            except Exception as e:
                list_of_errors.append(f'{tour.symbol} {e}')

        assert list_of_errors == [], f'The list of trips has errors: {list_of_errors}'
        assert list_of_errors > [], 'The offer will be published'


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('The offer of trips will be checked')
    Trip.publish_offer(trips)
    print('Done')
except Exception as e:
    print(f'The error occurred: {e}')
