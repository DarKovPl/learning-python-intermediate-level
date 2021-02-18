import datetime as dt


# class BITException(Exception):
#
#     def __init__(self, text, area):
#         super(BITException, self).__init__(text)
#         self.area = area
#
#     def __str__(self):
#         return f'{super().__str__()}, area {self.area}'
#
#
# class BITSecurityException(BITException):
#     pass
#
#
# class BITDataFormatException(BITException):
#     pass
#
#
# try:
#     # do something...
#     1/0
#     raise BITDataFormatException('file format is incorrect', 'Financial data')
# except BITSecurityException as e:
#     print(f'Application security error: {e}')
# except BITDataFormatException as e:
#     print(f'Application data malformed error: {e}')
# except BITException as e:
#     print(f'Application error: {e}')
# except Exception as e:
#     print(f'General error: {e}')

# Lab

class Trip:

    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Error; ")
        if self.start > self.end:
            raise TripDateException('Error;')

    @classmethod
    def publish_offer(cls, tours):

        list_of_errors = []

        for tour in tours:

            try:
                tour.check_data()
            except TripDateException as e:
                list_of_errors.append(f'{tour.symbol} {e.description}')
            except TripNameException as e:
                list_of_errors.append(f'{tour.symbol} {e.description}')

        if list_of_errors > []:
            raise TripException('The list of trips has errors:', list_of_errors)
        else:
            print('The offer will be published')


class TripException(Exception):

    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return f"""{super().__str__()}The description: {self.description}"""


class TripNameException(TripException):

    def __init__(self, text):
        super(TripNameException, self).__init__(text, 'Name of the trip is missing. '
                                                      'You need to name the trip somehow.')


class TripDateException(TripException):

    def __init__(self, text):
        super(TripDateException, self).__init__(text, 'The dates are incorrect. '
                                                      'The starting date should be earlier than the ending date.')


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
