class Boy:

    age= None

class Girl:

    age = None

def how_old(name, year):

    name.age = year

boy_1 = Boy()
boy_2 = Boy()
girl_1 = Girl()
girl_2 = Girl()

how_old(boy_1, 20)
how_old(boy_2, 30)
how_old(girl_1, 18)
how_old(girl_2, 25)

print(boy_2.age)
print(girl_1.age)
