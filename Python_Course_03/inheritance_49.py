class Pupils:

    def come(self):
        print('All pupils of school will come at 7.30')
    def go_home(self):
        print('All pupils of school go home at 14.30')
    def breakfast(self):
        print('The breakfast at school is at 12.00')

class Boy(Pupils):

    def run(self):
        print('Boys will run every morning about 4 km')

class Girl(Pupils):
    def run(self):
        print('Girls will run about 2 km')

boy = Boy()
girl = Girl()

boy.come()
boy.run()
girl.breakfast()
girl.go_home()
