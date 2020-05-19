
import turtle
class pentagon():
    def __init__(self,arr = 50):
        self.__sides = arr
    
    def get_sides(self):
        return self.__sides
    
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.__sides)
        t.left(72)
        t.forward(self.__sides)
        t.left(72)
        t.forward(self.__sides)
        t.left(72)
        t.forward(self.__sides)
        t.left(72)
        t.forward(self.__sides)
        turtle.done()

    def perimeter(self):
        return (self.__sides * 5)

print("Enter The length of side of perimeter")
side = int(input())
p = pentagon(side)
print("Side of pentagon is ",p.get_sides())
print("Perimeter is ", p.perimeter())
p.draw()