def multiple(x):
    return x ** 2

def divide(x):
    return x / 2

def cube(x):
    return x ** 3

def quadrate(x):
    return x ** 4

def add(x):
    return x + x

def finish(func):
    abra = func(10)
    print(abra)

finish(multiple)
finish(divide)
finish(cube)
