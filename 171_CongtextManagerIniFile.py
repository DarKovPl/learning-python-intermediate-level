import io
import os
import requests
import zipfile


# class IniFile:
#
#     def __init__(self, path):
#         print('__init__')
#         self.path = path
#         self.parameters = {}
#         self.read_from_disk()
#
#     def read_from_disk(self):
#         if os.path.isfile(self.path):
#             with open(self.path) as file:
#                 for line in file:
#                     parts = line.replace("\n", '').split('=')
#                     self.parameters[parts[0]] = parts[1]
#
#     def read_parameter(self, key):
#         if key in self.parameters.keys():
#             return self.parameters[key]
#         else:
#             return None
#
#     def write_parameter(self, key, value):
#         self.parameters[key] = value
#
#     def save_on_disk(self):
#         with open(self.path, "w") as file:
#             for key, value in self.parameters.items():
#                 line = f'{key}={value}\n'
#                 file.write(line)
#
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__')
#         pass
#
#
# ini = IniFile(r'/tmp/my.ini')
# ini.write_parameter('version', 1)
# ini.write_parameter('level', 'advanced')
# ini.save_on_disk()
#
# ini_2 = IniFile(r'/tmp/my.ini')
# print(ini_2.parameters)
# print(ini_2.read_parameter('version'))
# print(ini_2.read_parameter('level'))
#
#
# with IniFile(r'/tmp/my.ini') as ini_3:
#     print(ini_3.parameters)
#     print(ini_3.read_parameter('version'))
#     print(ini_3.read_parameter('level'))


# Lab


class DownloadFileFromSite:

    def __init__(self, address, disc_path_for_file):
        self.address = address
        self.save_on_disk_location = os.path.join(disc_path_for_file, self.get_zip_file_name)

    @property
    def download_file(self):
        r = requests.get(self.address)
        return r.content

    def save_file_on_disc(self):
        with open(self.save_on_disk_location, 'wb') as f:
            f.write(self.download_file)

    @property
    def get_zip_file_name(self):
        first_pos = str(self.address).rfind('/')
        zip_file_name = str(self.address[first_pos + 1:])
        return zip_file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


path = r'/tmp/'
web_address = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'

# test = DownloadFileFromSite(web_address, path)
# test.save_file_on_disc()


with DownloadFileFromSite(web_address, path) as test:
    z = zipfile.ZipFile(io.BytesIO(test.download_file))
    z.extractall(path)
