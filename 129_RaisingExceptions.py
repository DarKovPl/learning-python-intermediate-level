import datetime as dt


# def process_invoice(net, gross):
#     if net >= gross:
#         raise ValueError('Net value should be lower or equal to gross value.')
#     else:
#         print(f'Processing invoice: net={net}; gross={gross}')
#
#
# def end_of_month():
#     net_value = 1230
#     gross_value = 10000
#
#     try:
#         process_invoice(net_value, gross_value)
#     except ValueError as e:
#         print(f'The values on invoice are incorrect: {e}')
#         raise ValueError('Error when processing invoices') from e
#     except Exception as e:
#         print(f'Error processing invoice: {e}')
#         raise Exception('General error when processing invoices')
#
#
# end_of_month()


# Lab

class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, tours):

        list_of_errors = []

        for tour in tours:

            try:
                tour.check_data()
            except ValueError as e:
                list_of_errors.append(f'{tour.symbol} {e}')
            except Exception as e:
                list_of_errors.append(f'{tour.symbol} {e}')

        if list_of_errors > []:
            raise Exception(f'The list of trips has errors: {list_of_errors}')
        else:
            print('The offer will be published')


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

