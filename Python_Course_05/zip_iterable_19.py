username = ['Nuriddin', 'James', 'Carvajal', 'Modric']
parol = ['my_name', 'player', 'spanish', 'WC2018']
login = ['nuriddin_husinov', 'james', 'carvajal', 'modric']

file = dict(zip(username, parol))
print(type(file))

for key, value in file.items():
    print(key + ' : ' + value)

print('----------------------')

second_file = zip(username, parol, login)
for i in second_file:
    for j in i:
        print(j, end=' : ')
    print()
