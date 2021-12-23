store = [('Ronaldo', 187),
         ('Messi', 170),
         ('Aubameyang', 175),
         ('Carvajal', 177),
         ('Ramos', 185)]

player = lambda high : high[1] > 180

# def player(high):
#     if high[1] > 180:
#         return True
#     return False

highest = list(filter(player, store))
for i in highest:
    print(i)
