## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Code Examples](#code-examples)
## General Info
***
This repository shows the progress of learning Python programming.
## Screenshot
![Image text](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/downloads/release/python-369/): Version 3.6.9 
## Code Examples
***
Link to file: https://github.com/DarKowPl/learning-python-intermediate-level/blob/master/09_Generators/159_Itertools.py

Examples of code:
```python
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    
    value_of_song_notes = 4  # Here you can change the number of song notes
    
    var_without_rep = [note for note in it.permutations(notes, value_of_song_notes)]
    
    var_with_rep = [note for note in it.product(notes, repeat=value_of_song_notes)]
    
    factorial = lambda num: 1 if num <= 1 else num * factorial(num - 1)
    
    power = lambda num, power: num ** power
    
    
    def check_and_print(song_without_rep, song_with_rep, fact, pow, for_div):
    
        math_form = fact / for_div
        if (len(song_without_rep), len(song_with_rep)) == (math_form, pow):
            print(f'Amount of the variations WITHOUT repetition is correct, and the total is {int(math_form)}.',
                  f'Amount of the variations WITH repetition is correct, and the total is {pow}')
        else:
            raise Exception('Something went wrong. Please check arguments')
    
    
    to_factorial = functools.partial(factorial, len(notes))
    to_power = functools.partial(power, len(notes), value_of_song_notes)
    to_div = functools.partial(factorial, len(notes) - value_of_song_notes)
    for_check_and_print = functools.partial(check_and_print, var_without_rep, var_with_rep)
    
    for_check_and_print(to_factorial(), to_power(), to_div())
```
***

Link to file: https://github.com/DarKowPl/learning-python-intermediate-level/blob/master/07_ErrorHandling/129_RaisingExceptions.py

Examples of code:

```python
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
    
```
