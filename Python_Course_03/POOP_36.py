class Student:

    def __init__(self, name, year_of_born, height, GPA):
        self.name = name
        self.yob = year_of_born
        self.height = height
        self.GPA = GPA

    def detail(self):
        print('Student name: ' + self.name)
        print('Date of birth: ' + str(self.yob))
        print('Student height: ' + str(self.height))
        print('GPA of the student: ' + self.GPA)
    def exam(self):
        print('Did student pass the exam? ', end='')
        if float(self.GPA) >= 2.6:
            print('Yes')
        else:
            print('No')
        print('-------------------------------')
