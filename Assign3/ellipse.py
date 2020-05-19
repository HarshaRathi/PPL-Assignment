import turtle
import math
class ellipse():
    def __init__(self,radius = 100):
        self.__radius = radius
    def area(self):
        return (self.__radius * (self.__radius/2) * math.pi )
    def drawtalloval(self):
        t = turtle.Turtle()
        t.left(45)
        for loop in range(2):
            t.circle(self.__radius,90)
            t.circle(self.__radius/2,90)
        turtle.done()
print("Enter the radius of the circle")  
radius = int(input())
e = ellipse(radius)
print("Area of oval  =  ",e.area())
e.drawtalloval()