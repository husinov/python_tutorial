def summ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(summ(1, 2, 3, 4, 5, 6, 7, 8))

def little(*name):
    print('The youngest child is ' + name[1])

little('Jason', 'Sancho', 'Carvalho')

def multiply(*num):

    num = list(num)
    one = 1
    for i in num:
        one *= i
    print(type(num))
    return one
print(multiply(9, 12))
