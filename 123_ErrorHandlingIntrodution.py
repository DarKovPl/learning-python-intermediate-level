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
#     print(f'The % ratio for {my_client} is {clients[my_client]}.')
# except Exception as e:
#     print(f'Sorry we have an error....\nDetalis: {e}')
# else:
#     print(f"The cost for {my_client} is {clients[my_client] * total_cost}")
# finally:
#     print("-= Calculation finished =-")


# Lab

def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)

    with open(file_path, 'wb') as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = '/home/darek/Projects/to_task_123'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print(f'File already existed:: {os.path.split(tmpfile_path)[1]}'
              f' and was deleted.')
    else:
        save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print(f'Exception {e}')

else:
    print('Copying from website was successful')

finally:
    if os.path.isfile(tmpfile_path):
        os.remove(tmpfile_path)
        print(f'File already existed:: {os.path.split(tmpfile_path)[1]}'
              f' and was deleted.')
