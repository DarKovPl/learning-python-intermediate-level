import os
import sys
import urllib.request

# instruction = ['say hello', 'say how are you', 'abort', 'ask for money', 'say thank you']
# instruction_approved = []
#
# for instr in instruction:
#     print('Adding instruction: ', instr)
#     instruction_approved.append(instr)
#
#     if instr == 'abort':
#         print('Aborting!!!')
#         instruction_approved.clear()
#         break
#
# else:
#     print('Following actions will be taken: ', instruction_approved)
# print('-------------------------------------------------------------------')
#
# instruction_approved.clear()
# i = 0
#
# while len(instruction) > i:
#     print('Adding instruction: ', instruction[i])
#     instruction_approved.append(instruction[i])
#
#     if instruction[i] == 'abort':
#         print('Aborting!!!')
#         instruction_approved.clear()
#         break
#     i += 1
#
# else:
#     print('Following actions will be taken: ', instruction_approved)
print('-------------------------------------------------------------------')

# Lab

data_dir = r'/tmp/data_dir/'

if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

pages = [

    {'name': 'mobilo',          'url': 'http://www.mobilo24.eu/'},

{ 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    {'name': 'kursy',           'url': 'http://www.kursyonline24.eu/'}]

for page in pages:

    try:
        path = os.path.join(data_dir, page.get('name')) + '.html'
        print("Creating the file '{}' where will be saved content from the site.".format(path))

        urllib.request.urlretrieve(page.get('url'), path)
        print("Downloading data from the site: {}".format(page.get('url')))
        print('-' * 20)

    except:
        print('-' * 20)
        print('Error has occurred: "' + str(sys.exc_info()) + '" and the process was stopped.')
        break

else:
    print('Everything was done successfully.')
