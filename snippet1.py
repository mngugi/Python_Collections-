class Glasses:
    def printShadeIndex(self):
        print("low")


class Sunglasses(Glasses):
    def printShadeIndex(self):
        print("high")



glasses = Glasses()
glasses.printShadeIndex()
