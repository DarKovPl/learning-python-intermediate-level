import random

# file = open(r'/home/darek/Projects/to_task_153/data.txt')
#
# data = file.read()
#
# file.close()
#
# for line in data.splitlines():
#     if line.startswith('ACTION'):
#         print(line)
print('------------------------------------------------------------')

# file = open(r'/home/darek/Projects/to_task_153/data.txt')
#
# for line in file:
#     if line.startswith("ACTION"):
#         print(line.replace("\n", ''))
#
# file.close()
print('------------------------------------------------------------')


# file = open(r'/home/darek/Projects/to_task_153/data.txt')
# records = []
#
# for line in file:
#     if ':' in line:
#         type, action = line.rstrip('\n').split(':', 1)
#         record = (type, action)
#         records.append(record)
# print(records)
#
# file.close()
# print('------------------------------------------------------------')
#
#
# def get_records(file_path):
#     print('---opening file---')
#     file = open(file_path)
#
#     for line in file:
#         if ':' in line:
#             type, action = line.rstrip('\n').split(':', 1)
#             record = (type, action)
#             yield record
#
#     print('---closing file---')
#     file.close()
#
#
# for r in get_records(r'/home/darek/Projects/to_task_153/data.txt'):
#     print(f'The type is {r[0]} and the action is {r[1]}')
# print('------------------------------------------------------------')

# Lab

def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    numbers = list(range(number_of_values))

    while True:
        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randrange(1, 101)

        if sum(numbers) == asserted_sum:
            yield trial, numbers
            trial = 0


for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)
