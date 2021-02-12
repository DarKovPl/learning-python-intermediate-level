import time


# try:
#     with open(r'/home/darek/Projects/to_task_168/my_file.txt', 'w+') as file:
#         file.writelines('SUCCESS')
# except PermissionError as e:
#     print(f'Error opening the file {e.filename}, details: {e.strerror}')

# class TimeMeasure:
#
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         print('entering....')
#         self.__start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exiting...')
#         self.__stop = time.time()
#         self.__difference = self.__stop - self.__start
#         print(f'Execution time: {self.__difference}')
#
#
# with TimeMeasure() as my_timer:
#     time.sleep(3)
# print('----------------------------------------------------------------')
#
# with TimeMeasure():
#     time.sleep(3)

# Lab

class HtmlCm:

    def __init__(self):
        pass

    def __enter__(self):
        print('''
<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>''')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>"')


with HtmlCm() as html:
    print('''
<TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>''')
