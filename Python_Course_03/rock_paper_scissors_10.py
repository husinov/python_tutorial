import random
def won():
    print('Gongratulations! You won!')
def lost():
    print('You lost! Try again!')
def list():
    print('Computer:  ', computer)
    print('You chose: ', player)

while True:
    choices = ('rock', 'paper', 'scissors')
    computer = random.choice(choices)
    player = None
    while not player in choices:
        player = input('Choose from rock, paper and scissors: ').lower()
        if not player in choices:
            print('Choose from a list!')
        elif computer == player:
            list()
            print('Tie!')
        elif computer == 'rock':
            list()
            if player == 'paper':
                won()
            elif player == 'scissors':
                lost()
        elif computer == 'paper':
            list()
            if player == 'rock':
                lost()
            elif player == 'scissors':
                won()
        elif computer == 'scissors':
            list()
            if player == 'rock':
                won()
            elif player == 'paper':
                lost()
    try_again = input('Do you want to try again? Press yes/no! ').lower()
    if try_again != 'yes':
        break

print('Goodbye! I hope you liked this game!')
