name = 'Nuriddin'
sport = 'Golf'

print('Hello, my name is {}.'.format(name))
print('Hello, my name is {:50}.'.format(name))     #default
print('Hello, my name is {:<50}.'.format(name))    #left
print('Hello, my name is {:>50}.'.format(name))    #right
print('Hello, my name is {:^50}.'.format(name))    #center

print('Hello, my name is {:>25}. I like {:^25}.'.format(name, sport))      #position default
print('I like {1:^25}. Hello, my name is {0:<25}.'.format(name, sport))    #position numeration

print('I like {sport:>25}. His name is {name:^25}.'.format(name = 'Jordan', sport = 'Tennis')) #keyword
