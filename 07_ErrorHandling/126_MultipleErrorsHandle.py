import requests
import os
import shutil

# clients = {
#     "INFO": 0.5,
#     "DATA": 0.2,
#     "SOFT": 0.2,
#     "INTER": 0.1,
#     "OMEGA": 0.0
# }
#
# my_client = input("Enter client's name: ").upper()
# total_cost = 7200
#
# try:
#     ratio = float(input('Enter new ratio: '))
#     print(f'The default % ratio for {my_client} is {clients[my_client]}, a new one is {ratio}.')
#     print(f"The cost for {my_client} is {ratio * total_cost}")
#     print(f'The new ratio comparison to old ratio: {clients[my_client] / ratio}')
# except KeyError as e:
#     print(f'Client {my_client} is not on the list {[a for a in clients.keys()]}.\nDetails:\n{e}')
# except (ValueError, ZeroDivisionError) as e:
#     print(f'There is a problem with entered value for ratio - it must be a number greater than 0.\nDetail:\n{e}')
# # except ZeroDivisionError as e:
# #     print(f'The new ratio cannot be 0.\nDetails\n{e}')
# except Exception as e:
#     print(f'Sorry we have an error....\nDetails: {e}')


# Lab

def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)

    with open(file_path, 'wb') as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = '/home/darek/Projects/to_task_127/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print(f'File already existed:: {os.path.split(tmpfile_path)[1]}'
              f' and was deleted.')
    # else:
    #     save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as e:
    print('The webpage address:', f'"{e}"'.split("'")[1],
          'is improper.\nPlease to write the correct address.')
except PermissionError as e:
    print(f'The file "{os.path.basename(file_path)}" is only readable.'
          f' Please set the correct permissions in file. {e}')
except FileNotFoundError as e:
    print(f'The file:', f'{e}'.split("'")[1].split("/")[-1], 'does not exist in',
          f'{e}'.split("'")[1][:-len(''.join(a for a in f'{e}'.rsplit('/')[-1]))])
except Exception as e:
    print(f'Exception {e}')

else:
    print('Copying content from website was successful')

finally:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print(f'File: {os.path.split(tmpfile_path)[1]} was deleted.')
