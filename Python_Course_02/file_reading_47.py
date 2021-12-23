try:
    with open('test.txt') as file:
        print(file.read())
    print(file.name)
    # print(file.closed)
    #     for i in file:
    #         print(i)
except FileNotFoundError:
    print('There is no file, with such name!')