from Rectangle import Rectangle
import math
class Triangle(Rectangle):
    def __init__(self, cathetus_1, cathetus_2):
        super().__init__(cathetus_1, cathetus_2)

    def get_area(self):
        return (self.width * self.height)/2

    def get_perimeter(self):
        return math.sqrt(self.width**2 + self.height**2) + self.width + self.height