import time


# try:
#     with open(r'/home/darek/Projects/to_task_168/my_file.txt', 'w+') as file:
#         file.writelines('SUCCESS')
# except PermissionError as e:
#     print(f'Error opening the file {e.filename}, details: {e.strerror}')

class time_measure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering....')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print(f'Execution time: {self.__difference}')


with time_measure() as my_timer:
    time.sleep(3)
print('----------------------------------------------------------------')

with time_measure():
    time.sleep(3)

# Lab

