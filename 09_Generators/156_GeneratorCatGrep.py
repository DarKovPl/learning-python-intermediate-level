import os
import requests

# path = r'/home/darek/Projects/learning-python-intermediate-level'
# search_string = 'Ford'
# file_extension = '.py'
#
# for dir_name, sub_dirs, file_names in os.walk(path):
#     # print(dir_name, sub_dirs, file_names)
#     for file_name in file_names:
#         if file_name.endswith(file_extension):
#             full_file_name = os.path.join(dir_name, file_name)
#             for line in open(full_file_name):
#                 if search_string in line:
#                     print(file_name)
# print('--------------------------------------------------------------')
#
#
# def generate_files(base_dir, file_extension):
#     for dir_name, sub_dirs, file_names in os.walk(base_dir):
#         for file_name in file_names:
#             if file_name.endswith(file_extension):
#                 full_file_name = os.path.join(dir_name, file_name)
#                 yield full_file_name
#
#
# def grep_files(search_string, files):
#     for file in files:
#         with open(file) as text:
#             if search_string in text.read():
#                 yield file
#
#
# files_generator = generate_files(path, file_extension)
# for file in grep_files(search_string, files_generator):
#     print(file)
print('--------------------------------------------------------------')

#  Lab
with open(r'/home/darek/Projects/to_task_157/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open(r'/home/darek/Projects/to_task_157/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

path = '/home/darek/Projects/to_task_157'


def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file)


def gen_get_file_lines(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            yield line.rstrip('\n')


def check_webpage(url):
    try:
        response = requests.get(url)
        print('OK')
        return response.status_code == 200

    except Exception as e:
        print('NOK', f'The exeption: {e}')
        return False


for file in gen_get_files(path):
    for line in gen_get_file_lines(file):
        check_webpage(line)
