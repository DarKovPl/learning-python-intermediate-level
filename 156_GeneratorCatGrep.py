import os

path = r'/home/darek/Projects/learning-python-intermediate-level'
search_string = 'Ford'
file_extension = '.py'

for dir_name, sub_dirs, file_names in os.walk(path):
    # print(dir_name, sub_dirs, file_names)
    for file_name in file_names:
        if file_name.endswith(file_extension):
            full_file_name = os.path.join(dir_name, file_name)
            for line in open(full_file_name):
                if search_string in line:
                    print(file_name)
print('--------------------------------------------------------------')


def generate_files(base_dir, file_extension):
    for dir_name, sub_dirs, file_names in os.walk(base_dir):
        for file_name in file_names:
            if file_name.endswith(file_extension):
                full_file_name = os.path.join(dir_name, file_name)
                yield full_file_name


def grep_files(search_string, files):
    for file in files:
        with open(file) as text:
            if search_string in text.read():
                yield file


files_generator = generate_files(path, file_extension)
for file in grep_files(search_string, files_generator):
    print(file)
print('--------------------------------------------------------------')


#  Lab

