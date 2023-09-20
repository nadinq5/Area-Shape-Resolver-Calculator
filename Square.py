from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)



# my_square = Square(5)
# my_rectangle = Rectangle(5, 5)