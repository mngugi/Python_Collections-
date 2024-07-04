class Car:
    def printSize(self):
        print("small")

class Hatch_Back(Car):
    def printSize(self):
        super().printSize()
        print("medium")

hatch = Hatch_Back()
hatch.printSize()
    
