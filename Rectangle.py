from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2
