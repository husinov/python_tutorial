# Duck Typing

class Old:

    def walk(self):
        print('An old man is walking')
    def drink(self):
        print('He stopped and drunk water')

class Young:

    def walk(self):
        print('A young boy is running')

    def drink(self):
        print('He stopped and drunk Pepsi')

class Person:

    def line(self, finish):
        finish.walk()
        finish.drink()
        print('He finished his line')

old = Old()
boy = Young()
person = Person()

person.line(boy)
print('------------------')
person.line(old)
