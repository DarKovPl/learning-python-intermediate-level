import itertools as it
import os
import re

# file_path = r'/home/darek/Projects/to_task_162/data.txt'
#
# data = []
#
# with open(file_path, 'r') as file:
#     for line in file:
#         elements = line.rstrip('\n').split(':')
#         d = {'type': elements[0], 'action': elements[1]}
#         data.append(d)
#
# data = sorted(data, key=lambda x: x['type'])
#
# for key, elements in it.groupby(data, key=lambda x: x['type']):
#     print(f'The key is {key} and the number of elements is {len(list(elements))}')


# Lab
path = '/home/darek/Projects'


def scan_tree(path):
    with os.scandir(path) as list:
        for obj in list:
            if obj.is_dir():
                yield obj
                yield from scan_tree(obj.path)
            else:
                yield obj


listing = scan_tree(path)
df = scan_tree(path)

for elem in listing:
    print(elem.path)
print('-----------')
df = sorted(df, key=lambda x: x.is_dir())

for bool, elem_1 in it.groupby(df, key=lambda x: x.is_dir()):
    print(f'The number of catalogs in {path.rsplit("/")[-1]} is {len(list(elem_1))}'
          if bool else f'The number of files in {path.rsplit("/")[-1]} is {len(list(elem_1))}')
