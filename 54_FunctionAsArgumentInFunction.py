def bake(what):
    print('Baking {}'.format(what))


def add(what):
    print('Adding {}'.format(what))


def mix(what):
    print('Mixing {}'.format(what))


cookbook = [(add, 'milk'), (add, 'eggs'), (add, 'flour'), (add, 'sugar'),
            (mix, 'ingredients'), (bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)
print('--------------')


def cook(activity, obj):
    activity(obj)


cook(bake, 'brownies')
print('--------------')

for activity, obj in cookbook:
    cook(activity, obj)

# Lab

