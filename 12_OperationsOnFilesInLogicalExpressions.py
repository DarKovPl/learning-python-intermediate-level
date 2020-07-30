import os


# path = r'/tmp/mydata.txt'

# os.remove(path)

# if os.path.isfile(path):
#     print('File %s exists' % path)
#
# else:
#     print('Creating a file %s' % path)
#     open(path, 'x').close()
#     print('File %s created' % path)

# result = os.path.isfile(path) or open(path, 'x').close()
# print(result)

# Lab

def count_words(path):
    #
    with open(path, 'r') as file:
        counted_words = len(str(file.read()).split(' '))
        return counted_words


path = r'/tmp/impossible'

if os.path.isfile(path):
    print('File has', count_words(path), 'words.')

# result = os.path.isfile(path) and print('File has', count_words(path), 'words...')
# print(result)
