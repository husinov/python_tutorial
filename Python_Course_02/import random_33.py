import random

x = random.randint(10,20)
print(x)

y = random.random()
print(y)

my_list = ['King', 'Lion', 'Cow', 'Eggle']
print(random.choice(my_list))

new_list = [1, 2, 3, 4, 5]
random.shuffle(new_list)
print(new_list)

print(random.choices(my_list, weights=(4, 1, 1, 1), k = 9))
