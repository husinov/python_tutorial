pls = ['Robben', 'Ronaldo', 'Messi', 'Carvalho']

pls[0] = 'Lewandowski'
num = ['Shevchenko', 'Lampard']

pls.append('Beckham')
# pls.clear()
a = pls.copy()
a = pls.count('Messi')
pls.extend(num)
a = pls.index('Ronaldo')
pls.insert(2, 'Carvajal')
pls.pop()
pls.remove('Messi')
pls.reverse()
pls.sort()

for i in pls:
    print(i)
