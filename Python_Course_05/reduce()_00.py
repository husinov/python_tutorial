import functools

# factorial = []
# n = int(input('Enter: '))
# if n == 0:
#     print('The answer is: 1')
# else:
#     for i in range(1, n + 1):
#         factorial.append(i)
#
#     result = functools.reduce(lambda x, y : x * y, factorial)
#
#     print('The answer is:', result)

name = ['C', 'A', 'R', 'V', 'A', 'J', 'A', 'L']

new = functools.reduce(lambda x, y : x + ' ' + y.lower(), name)

print(new)
