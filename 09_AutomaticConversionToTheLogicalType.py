# is_ok = True
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = 'True'
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = ''
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = 1
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = 0
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = -1
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = [1, 2, 3]
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = []
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = [0, 0, 0]
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# is_ok = [0, 0, 0]
# print("Variable is_ok: ", is_ok, type(is_ok))
# if is_ok[0]:  # reference to a list item zero
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# list_of_errors = [100, 101, 102]
# print("Variable list_of_errors: ", list_of_errors, type(list_of_errors))
# if list_of_errors:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# list_of_errors = [100, 101, 102]
# print("Variable list_of_errors: ", list_of_errors, type(list_of_errors))
# if len(list_of_errors) > 0:
#     print('TRUE')
# print('-------------------------------------------------------------------')
#
# Lab

option_list = [' load data', ' export data', ' analyze & predict']
chosen_option = 0

#  The loop will be working as far as the chosen_option value is
#  below or above range or entered character is improper
while not chosen_option:

    try:
        # here user enter of his choice, but before that he see the list of option to choose
        # and its assigned number to written.
        chosen_option = input('Please choose one of the options: \n{}.'
                              '\nEnter the number of your choice here -->'
                              .format('\n'.join(str(num + 1) + elem
                                                for num, elem in zip(range(len(option_list)), option_list))))

        if not chosen_option:
            print('You entered the enter key and program has been closed.')
            break

        elif 0 < int(chosen_option) <= 3:
            print('You chosen: {0:d}{1:s}'.format(int(chosen_option), option_list[int(chosen_option) - 1]))

        # if value of his choice is improper user will be informed what a mistake he did,
        # and the loop start again
        else:
            print("Your entered value '%d' is above the range" % int(chosen_option) if int(chosen_option) > 3
                  else "Your entered value '%d' is below the range" % int(chosen_option))
            chosen_option = 0

    # if user enter something else to integer program show him what is wrong and the loop start again
    except ValueError as e:
        print("\nThis error has occurred: '%s'." % e, 'Please enter the correct INT value from list.')
        chosen_option = 0





# def DisplayOptions(options):
#     for i in range(len(options)):
#         print("{} - {}".format(i + 1, options[i]))
#
#     choice = input('Select option above or press enter to exit: ')
#     return choice
#
#
# choice = 'x'
# options = ['load data', 'export data', 'analyze & predict']
#
# while choice:
#
#     choice = DisplayOptions(options)
#
#     # executed only if something was entered
#     if choice:
#         try:
#             choice_num = int(choice) - 1
#             if choice_num >= 0 and choice_num < len(options):
#                 print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
#             else:
#                 print("choose a value from a list or press enter")
#         except:
#             print("You need to enter a number")
#     else:
#         print('----- END -----')
