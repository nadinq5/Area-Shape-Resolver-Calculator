from Shape import Shape
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius**2*math.pi
