class Grandfather:

    def family(self):
        print('Jacksons are very tall.')

class Father(Grandfather):

    def relativity(self):
        print('He is Donald\'s father, Mr. Ronald Jackson.')

class Son(Father):

    def character(self):
        print('He\'s weight is approximately 80 kg.')

boy = Son()

boy.family()
boy.relativity()
boy.character()
