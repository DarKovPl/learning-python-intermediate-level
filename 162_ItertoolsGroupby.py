import itertools as it
import os


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

def scan_tree(path):
    for obj in os.scandir(path):
        if obj.is_dir():
            yield obj
            yield from scan_tree(obj.path)
        else:
            yield obj


listing = scan_tree('/home/darek/Projects')
