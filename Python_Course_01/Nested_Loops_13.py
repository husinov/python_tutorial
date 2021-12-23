from random import randint, randrange
from time import sleep

rows = int(input('How many rows? '))
columns = int(input('How many columns? '))
# symbol = input('Enter: ')

for j in range(columns):
    for i in range(rows):
        print(randrange(3, 9), end = ' ')
        sleep(0.05)
    print()
