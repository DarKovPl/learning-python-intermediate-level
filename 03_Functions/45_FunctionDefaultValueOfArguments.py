def buy_me(prefix='Please buy me', what='something nice.'):
    print(prefix, what)


buy_me('Please bu me', 'a new car')
buy_me(prefix='Please buy me', what='a car')
buy_me(what='a brand new car', prefix='Please buy me')
buy_me('Please')
buy_me(prefix='Please buy me')
buy_me(what='something sweet.')
print('-------------------------------------------------------------------')


# Lab

def show_progress(how_many, character='*'):
    print(character * how_many)


show_progress(10)
show_progress(15)
show_progress(30)
show_progress(10, '-')
show_progress(15, '+')
