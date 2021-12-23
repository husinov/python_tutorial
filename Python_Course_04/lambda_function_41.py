# def multiply(x):
#     return x * 2
# print(multiply(5))

# multiply = lambda x : x * 2
# print(multiply(4))
# divide = lambda x, y : x / y
# print(divide(16, 4))
# add = lambda x, y, z : x + y + z
# print(add(3, 4, 5))
# name = lambda first_name, last_name : first_name + ' ' + last_name
# print(name('Nuriddin', 'Husinov'))
age = lambda a : 'You can\'t visit us' if a < 18 else 'You can come to us'
print(age(18))

def func(x):
    return lambda y : x * y

nice = func(4)
print(nice(9))

print((lambda x : x)(4))