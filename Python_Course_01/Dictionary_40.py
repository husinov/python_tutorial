capitals = {'O\'zbekiston':'Toshkent',
            'Russia':'Moscow',
            'USA':'Washington DC',
            'England':'London',
            'Germany':'Berlin'}
capitals['Japan'] = 'Tokyo'

# fromkeys()
student = ('A', 'B', 'C', 'D', 'E')
degree = 5
journal = dict.fromkeys(student, degree)
for i,j in journal.items():
     print(i, ' - ', j)

print(capitals['O\'zbekiston'])
print(capitals.get('O\'zbekiston'))

print(capitals.items())
print(capitals.keys())
capitals.pop('USA')
capitals.popitem()
print(capitals.setdefault('China', 'Beijing'))
print(capitals.values())

capitals['Tadjikistan'] = 'Dushanbe'
capitals.update({'Tadjikistan':'Dushanbe'})

for i,j in capitals.items():
    print(i, ' - ', j)
