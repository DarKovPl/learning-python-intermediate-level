class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print(f'Opening the door to the {self.where}')

    def close(self):
        print(f'Closing door to the {self.where}')


door_1 = Door('hell')
door_2 = Door('future')

print('-----1-----')

door_1.open()
door_1.close()
print('---------------------------------------')

door_2.open()
door_2.close()
print('---------------------------------------')


from contextlib import contextmanager


@contextmanager
def open_and_close(obj):
    obj.open()
    yield obj
    obj.close()


with open_and_close(Door('next room')) as door:
    print(f'The door is to the {door.where}')
print('-------------------------------------------------------------------------')

print('-----2-----')


@contextmanager
def only_close(obj):     # Close
    yield obj
    obj.close()


with only_close(Door('next room')) as door:
    door.close()
    print(f'The door is to the {door.where}')
print('---------------------------------------')

from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('https://www.kursyonline24.eu/')) as page:  # Close
    for num, line in enumerate(page):
        if num <= 5:
            print(line)
print('-------------------------------------------------------------------------')

print('-----3-----')

import os

# os.remove(r'/tmp/not_used_file.txt')
print('---------------------------------------')

from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove(r'/tmp/not_used_file.txt')
print('-------------------------------------------------------------------------')

print('-----4-----')

from contextlib import redirect_stdout

f = open(r'/tmp/log.txt', 'w')
with redirect_stdout(f):
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()


# Lab

