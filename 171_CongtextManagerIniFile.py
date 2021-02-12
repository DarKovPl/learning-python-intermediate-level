import os


class IniFile:

    def __init__(self, path):
        print('__init__')
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace("\n", '').split('=')
                    self.parameters[parts[0]] = parts[1]

    def read_parameter(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameter(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, "w") as file:
            for key, value in self.parameters.items():
                line = f'{key}={value}\n'
                file.write(line)

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        pass


ini = IniFile(r'/tmp/my.ini')
ini.write_parameter('version', 1)
ini.write_parameter('level', 'advanced')
ini.save_on_disk()

ini_2 = IniFile(r'/tmp/my.ini')
print(ini_2.parameters)
print(ini_2.read_parameter('version'))
print(ini_2.read_parameter('level'))


with IniFile(r'/tmp/my.ini') as ini_3:
    print(ini_3.parameters)
    print(ini_3.read_parameter('version'))
    print(ini_3.read_parameter('level'))
