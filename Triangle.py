from Rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, cathetus_1, cathetus_2):
        super().__init__(cathetus_1, cathetus_2)

    def get_area(self):
        return (self.cathetus_1 * self.cathetus_2)/2
