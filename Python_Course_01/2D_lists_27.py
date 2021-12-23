players = ['Ronaldo', 'Messi', 'Neymar']
managers = ['Zidane', 'Tuchel', 'Mancini']
goalkeepers = ['Donnarumma', 'Navas', 'De Gea']

football_relation = [players, managers, goalkeepers]

# print(football_relation[1][2])

for i in football_relation:
    for j in i:
        print(j, end = ' ')
    print()