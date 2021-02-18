import requests
import zipfile
import contextlib
import os


# class Door:
#
#     def __init__(self, where):
#         self.where = where
#
#     def open(self):
#         print(f'Opening the door to the {self.where}')
#
#     def close(self):
#         print(f'Closing door to the {self.where}')
#
#
# door_1 = Door('hell')
# door_2 = Door('future')
#
# print('-----1-----')
#
# door_1.open()
# door_1.close()
# print('---------------------------------------')
#
# door_2.open()
# door_2.close()
# print('---------------------------------------')
#
# from contextlib import contextmanager
#
#
# @contextmanager
# def open_and_close(obj):
#     obj.open()
#     yield obj
#     obj.close()
#
#
# with open_and_close(Door('next room')) as door:
#     print(f'The door is to the {door.where}')
# print('-------------------------------------------------------------------------')
#
# print('-----2-----')
#
#
# @contextmanager
# def only_close(obj):  # Close
#     yield obj
#     obj.close()
#
#
# with only_close(Door('next room')) as door:
#     door.close()
#     print(f'The door is to the {door.where}')
# print('---------------------------------------')
#
# from urllib.request import urlopen
# from contextlib import closing
#
# with closing(urlopen('https://www.kursyonline24.eu/')) as page:  # Close
#     for num, line in enumerate(page):
#         if num <= 5:
#             print(line)
# print('-------------------------------------------------------------------------')
#
# print('-----3-----')
#
# import os
#
# # os.remove(r'/tmp/not_used_file.txt')
# print('---------------------------------------')
#
# from contextlib import suppress
#
# with suppress(FileNotFoundError):
#     os.remove(r'/tmp/not_used_file.txt')
# print('-------------------------------------------------------------------------')
#
# print('-----4-----')
#
# from contextlib import redirect_stdout
#
# f = open(r'/tmp/log.txt', 'w')
# with redirect_stdout(f):
#     print('Hello')
#     d = Door('EXIT')
#     d.open()
#     d.close()


# Lab

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        # if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)


with contextlib.suppress(FileNotFoundError):
    with contextlib.closing(FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
                                        r'/tmp/eurofxref_1.zip')) as f:
        f.download_file()

        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir(r'/tmp/')
            z.extract(a_file, '.', None)
        os.remove(f.tmp_file)
