class Animal:

    def drink(self):
        print('This animal is drinking')

class Cow(Animal):

    def drink(self):
        print('This cow is drinking water') #we use this one

cow = Cow()
cow.drink()
