from Shape import Shape
from Rectangle import Rectangle
from Square import Square
from Hexagon import Hexagon
from Triangle import Triangle
from Circle import Circle

shape_1 = Shape()
try:
    shape_1.get_area()
    shape_1.get_perimeter()
    shape_2 = Shape(4)
except:
    print("Shape is an interface class, cannot make instance Shape")



rec = Rectangle(1, 2)
print(rec)

sqr = Square(4)
print(sqr)

tri = Triangle(2, 3)
print(tri)

cir = Circle(4)
print(cir)

hex = Hexagon(3)
print(hex)