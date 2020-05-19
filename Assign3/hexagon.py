
import turtle
class hexagon():
    def __init__(self,arr = 50):
        self.__sides = arr
    
    def get_sides(self):
        return self.__sides
    
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.__sides)
        t.left(60)
        t.forward(self.__sides)
        t.left(60)
        t.forward(self.__sides)
        t.left(60)
        t.forward(self.__sides)
        t.left(60)
        t.forward(self.__sides)
        t.left(60)
        t.forward(self.__sides)
        turtle.done()

    def perimeter(self):
        return (self.__sides * 6)

print("Enter The length of side of hexagon")
side = int(input())
p = hexagon(side)
print("Side of pentagon is ",p.get_sides())
print("Perimeter is ", p.perimeter())
p.draw()