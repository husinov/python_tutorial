store = [('Ronaldo', 187),
         ('Messi', 170),
         ('Aubameyang', 175),
         ('Carvajal', 177),
         ('Ramos', 185)]

call = lambda player : (player[0], round(player[1]/3, 2))

store_new = list(map(call, store))

for i in store_new:
    for j in i:
        print(j, end = ' ')
    print()
