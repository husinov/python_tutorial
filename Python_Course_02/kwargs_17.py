def children(**kwargs):
    print('My oldest child\'s name is ', kwargs['first'] + '.')
children(first = 'Carlos', second = 'Tevez', third = 'Jackson')

def position(**player):
    for key, value in player.items():
        print(value, end = ' ')
position(CB = 'Ramos', MF = 'O\'zil', DB = 'Boateng')
