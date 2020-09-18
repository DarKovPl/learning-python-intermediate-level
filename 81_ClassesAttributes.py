class Car:

    def __init__(self, brand, model, is_airbag_ok, is_painting_ok, is_mechanic_ok):
        self.brand = brand
        self.model = model
        self.is_airbag_OK = is_airbag_ok
        self.is_painting_OK = is_painting_ok
        self.is_mechanic_OK = is_mechanic_ok


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.is_airbag_OK, car_01.is_painting_OK,
      car_01.is_mechanic_OK)
print(car_02.brand, car_02.model, car_02.is_airbag_OK, car_02.is_painting_OK,
      car_02.is_mechanic_OK)


# Lab

class Cake:

    def __init__(self, name, kind, taste, addictions, filling, wage):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.wage = wage


cake_01 = Cake('Pear-Ginger Pie', 'Pie', 'Ginger', addictions=['large pears', 'sugar', 'crystallized ginger',
                                                               'cornstarch', 'orange juice', 'cinnamon'],
               filling='Stuffed with pears', wage=1.8)

cake_02 = Cake('Italian Rainbow', 'Cookies', 'Raspberry jam', addictions=['Almonds', 'eggs',
                                                                          'cup of raspberry jam',
                                                                          'semisweet chocolate'],
               filling='Layers of almond and coated in chocolate', wage=0.5)
cake_03 = Cake('Banana Cream', 'Pie', 'Almond-Banana Cream', addictions=['Almond cream', 'medium bananas',
                                                                         'whipping cream', 'flour'],
               filling='Covered whipping cream', wage=0.9)

bakery_offer = [cake_01, cake_02, cake_03]

print("Today's offer is:")
for elm in bakery_offer:
    print(f"{elm.name} - ({elm.kind}) main taste: {elm.taste} with additives of {elm.addictions} filed with"
          f" {elm.filling} total weight: {elm.wage}\n", '-' * 60)
