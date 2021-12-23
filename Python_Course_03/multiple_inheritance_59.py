class Animal:

    def alive(self):
        print('This animal is alive')

class Prey(Animal):

    def flee(self):
        print('This animal flees')

class Predator(Animal):

    def hunt(self):
        print('This animal is hunting')

class Mouse(Prey):

    def run(self):
        print('This rat is running from cat')

class Snake(Predator):
    def eat(self):
        print('This snake is eating something')

class Cat(Prey, Predator):
    def wtdo(self):
        print('Is this cat running from sth or after sth?')

cat = Cat()
rat = Mouse()
snake = Snake()

# cat.alive()
# cat.wtdo()
# cat.flee()

# rat.alive()
# rat.flee()
# rat.run()

snake.alive()
snake.eat()
snake.hunt()
