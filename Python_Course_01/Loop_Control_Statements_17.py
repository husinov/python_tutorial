print('Break!')

while True:
    name = input('Enter your name: ')
    if name != '':
        break
print('Hello ' + name)

print('\nContinue!')

all = '144313037342340443434343334340314'
for i in all:
    if i == '4'  or i == '3':
        continue
    print(i, end = '')

print('\n\nPass!')

for i in range(1, 21):
    if i == 13 or i == 20:
        pass
    else:
        print(i)
