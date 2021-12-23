from random import randint

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Square(Rectangle):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)
    def area(self):
        return self.lenght * self.width

class Cube(Rectangle):
    def __init__(self, lenght, width, height):
        super().__init__(lenght, width)
        self.height = height

    def volume(self):
        return self.lenght * self.width * self.height

cube = Cube(randint(1, 5), randint(1, 5), randint(1, 5))
square = Square(randint(1, 5), randint(1, 5))
print('The volume of cube is equal to', cube.volume())
print('The area of squar is equal to', square.area())
print(cube.lenght, cube.width, cube.height)
print(square.lenght, square.width)
