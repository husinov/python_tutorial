import time

player = {'Navas' : 187, 'Ronaldo' : 187, 'Messi' : 170, 'Ramos' : 185}

# player_list = {key: round(value / 9 * 5, 1) for (key, value) in player.items()}
# print(player_list)

# player_list = {first: second for (first, second) in player.items() if second >= 180}
# print(player_list)

# player_list = {one: ('YES' if two < 187 else 'NO') for (one, two) in player.items()}
# print(player_list)

def click(one):
    if one > 185:
        return 'They are 3'
    elif one < 185:
        return 'They are 2'
    else:
        return 'I didn\'t count'

player_list = {key: click(one) for (key, one) in player.items()}
print(player_list)

print(time.perf_counter())
