my_var = 'Hello Pycharm'
my_var_2 = my_var + '!!'
print(my_var, '---', my_var_2)
print(type(my_var), type(my_var_2))
print('Is value the same?', my_var == my_var_2)
print('Are the variables the same?', my_var is my_var_2)
print(id(my_var), id(my_var_2))
print('-------------------------------------------------------------------')

my_var_2 = my_var_2[:-2]
print(my_var, '---', my_var_2)
print(type(my_var), type(my_var_2))
print('Is value the same?', my_var == my_var_2)
print('Are the variables the same?', my_var is my_var_2)
print(id(my_var), id(my_var_2))
print('-------------------------------------------------------------------')

# Lab
a = b = c = 10

print(a, b, c)
print(id(a), id(b), id(c))

a = 20

print(a, b, c)
print(id(a), id(b), id(c))
print('-------------------------------------------------------------------')

a = b = c = [1, 2, 3]

print(a, b, c)
print(id(a), id(b), id(c))

a.append(4)

print(a, b, c)
print(id(a), id(b), id(c))
print('-------------------------------------------------------------------')

x = 10
y = 10
print(id(x), id(y))

y = y + 1 - 1
print(id(x), id(y))

y = y + 1234567890 - 1234567890
print(id(x), id(y))
print('-------------------------------------------------------------------')
