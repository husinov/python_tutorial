number = 3.14159
num = 10000000

print('The pi is equal to {:.3f}.'.format(number))
print('The pi is equal to {:.2f}.'.format(number))
print('The pi is equal to {0:.3f}.'.format(number))                        #position
print('The pi is equal to {number:.6f}.'.format(number = 3.14159829392))   #keyword

print('My number is equal to {:,}'.format(num))
print('My number is equal to {:b}'.format(num))
print('My number is equal to {:o}'.format(num))

print('My number is equal to {:x}'.format(num))
print('My number is equal to {:X}'.format(num))

print('My number is equal to {:E}'.format(num))
print('My number is equal to {:e}'.format(num))
