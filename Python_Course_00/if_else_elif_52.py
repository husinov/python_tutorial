while True:

    age = int(input('How old are you? '))

    if age >= 18:
        print('You are free to go!')
    elif age < 7:
        print('First you have to go to school!')
    else:
        print('Stay here, you will go with your teacher!')
