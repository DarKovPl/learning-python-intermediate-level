clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

my_client = input("Enter client's name: ").upper()
total_cost = 7200

try:
    ratio = float(input('Enter new ratio: '))
    print(f'The default % ratio for {my_client} is {clients[my_client]}, a new one is {ratio}.')
    print(f"The cost for {my_client} is {ratio * total_cost}")
    print(f'The new ratio comparison to old ratio: {clients[my_client] / ratio}')
except KeyError as e:
    print(f'Client {my_client} is not on the list {[a for a in clients.keys()]}.\nDetails:\n{e}')
except (ValueError, ZeroDivisionError) as e:
    print(f'There is a problem with entered value for ratio - it must be a number greater than 0.\nDetail:\n{e}')
# except ZeroDivisionError as e:
#     print(f'The new ratio cannot be 0.\nDetails\n{e}')
except Exception as e:
    print(f'Sorry we have an error....\nDetails: {e}')

