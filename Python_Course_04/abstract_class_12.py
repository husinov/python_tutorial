from abc import ABC, abstractmethod

class Students(ABC):

    @abstractmethod
    def run(self):
        pass
    @abstractmethod
    def learn(self):
        pass

class Jason(Students):
    def run(self):
        print('Jason has to run about 2 km')
    def learn(self):
        print('Jason good at math and physics')

class Jordan(Students):
    def run(self):
        print('Jordan can run 3 km without stopping')
    def learn(self):
        print('Jordan has high degree at chemistry and biology')

jason = Jason()
jordan = Jordan()

jason.run()
jordan.run()

jason.learn()
jordan.learn()
