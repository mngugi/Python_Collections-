class Compare:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __bool__(self):
        return  self.a is self.b

c1 = Compare([1,2,3], [1,2,3])

print(c1.__bool__())

