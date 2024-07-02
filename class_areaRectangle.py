class Rectangle:
    def __init__(self, a_val, b_val):
        self.a = a_val
        self.b = b_val

    def calculate_area_rectangle(self):
        return self.a * self.b


rectangle = Rectangle(5, 2)
print(rectangle.calculate_area_rectangle())
