student = ('Nuriddin', 20, 'TUIT')

print(student.count(20))
print(student.index('TUIT'))

for i in student:
    print(i)

if 'Nuriddin' in student:
    print('Nuriddin is a student!')

print(type(student))
