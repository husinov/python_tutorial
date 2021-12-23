def hello():
    print('Hello man!')
hello()

def hello(name):
    print('My name is ' + name + '.')
hello('Nuriddin')

def hello(first_name, second_name, age):
    print('My full name is ' + second_name + ' ' + first_name + '.')
    print('I\'m ' + str(age) + ' years old.')
hello('Nuriddin', 'Husinov', 20)
