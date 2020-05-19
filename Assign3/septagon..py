
import turtle
class septagon():
    def __init__(self,arr = 50):
        self.__sides = arr
    
    def get_sides(self):
        return self.__sides
    
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        t.left(51.43)
        t.forward(self.__sides)
        turtle.done()

    def perimeter(self):
        return (self.__sides * 7)

print("Enter The length of side of septagon")
side = int(input())
p = septagon(side)
print("Side of septagon is ",p.get_sides())
print("Perimeter is ", p.perimeter())
p.draw()