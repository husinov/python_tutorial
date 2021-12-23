# foods = []
#
# while bool := (food := input('What do you want to it? ')) != 'q':
#     foods.append(food)
# print(foods)
# print(bool)

# Both mean one thing

# name = 'Nuriddin Husinov'
# print(name)

# print(name := 'Nuriddin Husinov')

# Both mean one thing

# country = ['USA', 'Russia', 'Uzbekistan']
# for i in country:
#     print(i, end=' ')

for i in (country := ['USA', 'Russia', 'Uzbekistan']):
    print(i, end=' ')
