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
pages = [

    {'name': 'mobilo',          'url': 'http://www.mobilo24.eu/'},

    {'name': 'nonexistent',     'url': 'http://abc.cde.fgh.ijk.pl/'},

    {'name': 'kursy',           'url': 'http://www.kursyonline24.eu/'}]

for page in pages:

    try:

        path = data_dir + page.get('name') + '.html'
        urllib.request.urlretrieve(page.get('url'), path)


    except:
        print(sys.exc_info())
        break

else:
    print('ok')
