class Technique:
    def robot(self, it):
        pass

class Robot(Technique):
    def see(self):
        print(it + ' can see this')
        return self
    def pen(self):
        print(it + ' took a pen to his hand')
        return self
    def write(self):
        print(it + ' wrote a letter')
        return self

robot = Robot()
it = 'Carlos'

# robot.see()\
#     .pen()\
#     .write()

robot.see().pen().write()
