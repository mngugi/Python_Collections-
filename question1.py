class Compare:
    def __init__(self,apple,banana):
        self.apple = apple
        self.banana = banana

    def __bool__(self):
        return  self.apple is self.banana

c1 = Compare([1,2,3], [1,2,3])

print(c1.__bool__())

