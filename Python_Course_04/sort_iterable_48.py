players = [('James', 180, 25),
           ('Drogba', 185, 30),
           ('Lampard', 183, 32),
           ('Gerrard', 176, 24)
           ]

age = lambda ages : ages[2]
players.sort(key = age, reverse = False)
for i in players:
    print(i)
print('--------------------')
players = (('James', 180, 25),
           ('Drogba', 185, 30),
           ('Lampard', 183, 32),
           ('Gerrard', 176, 24)
           )

# def height(high):
#     return high[1]
height = lambda high : high[1]

sorted_players = sorted(players, key = height, reverse = True)

for j in sorted_players:
    for n in j:
        print(n, end = ' ')
    print()
