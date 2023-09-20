from Shape import Shape
import math
class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (3 * math.sqrt(3) * self.side_length**2 /2)

    def get_perimeter(self):
        return self.side_length*6

    def __str__(self):
        return (f'{self.get_area()}')