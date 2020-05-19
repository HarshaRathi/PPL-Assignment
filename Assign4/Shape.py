import turtle as t
import math
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Line(Shape):
    def __init__(self,length = 50):
        self.__length = length

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.__length)
        #turtle.done()

    def get_length(self):
        return self.__length

    def set_length(self,length):
        self.__length = length


class Polygon(Shape):
    def __init__(self,sides):
        self.sides =  sides
    def get_sides(self):
        return self.sides
    def set_sides(self,sides):
        self.sides = sides
    def perimeter(self):
       pass
    
class Rectangle(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def area(self):
        return (self.sides[0] * self.sides[1])

    def perimeter(self):
        return(2 * sum(self.sides))
    
    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides[0])
        t.left(90)
        t.forward(self.sides[1])
        t.left(90)
        t.forward(self.sides[0])
        t.left(90)
        t.forward(self.sides[1])
        #turtle.done()


class Square(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def area(self):
        return (self.sides * self.sides)

    def perimeter(self):
        return(4 * self.sides)

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides)
        t.left(90)
        t.forward(self.sides)
        t.left(90)
        t.forward(self.sides)
        t.left(90)
        t.forward(self.sides)
        #turtle.done()

class Pentagon(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def perimeter(self):
        return(5*self.sides)

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides)
        t.left(72)
        t.forward(self.sides)
        t.left(72)
        t.forward(self.sides)
        t.left(72)
        t.forward(self.sides)
        t.left(72)
        t.forward(self.sides)
        #turtle.done()

class Hexagon(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def perimeter(self):
        return(6*self.sides)

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides)
        t.left(60)
        t.forward(self.sides)
        t.left(60)
        t.forward(self.sides)
        t.left(60)
        t.forward(self.sides)
        t.left(60)
        t.forward(self.sides)
        t.left(60)
        t.forward(self.sides)
        #turtle.done()

class Heptagon(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def perimeter(self):
        return(7*self.sides)

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        t.left(51.43)
        t.forward(self.sides)
        #turtle.done()

class Parallelogram(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def perimeter(self):
        return(2 * sum(self.sides))

    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides[0])
        t.left(135)
        t.forward(self.sides[1])
        t.left(45)
        t.forward(self.sides[0])
        t.left(135)
        t.forward(self.sides[1])
        #turtle.done()


class Triangle(Polygon):
    def __init__(self,sides):
        Polygon.__init__(self,sides)

    def perimeter(self):
        return(sum(self.sides))

    
class EquiTriangle(Triangle):
    def __init__(self,sides):
        Triangle.__init__(self,sides)
    
    def draw(self):
        #t = turtle.Turtle()
        t.forward(self.sides[0])
        t.left(120)
        t.forward(self.sides[0])
        t.left(120)
        t.forward(self.sides[0])
        #turtle.done()

    def area(self):
        return ((math.sqrt(3)/4)*(self.sides[0]*self.sides[0]))

class RightAngleTriangle(Triangle):
    def __init__(self,sides):
        Triangle.__init__(self,sides)
    
    def draw(self):
        #t = turtle.Turtle()
        #t.right(90)
        t.forward(self.sides[0])
        t.left(90)
        t.forward(self.sides[1])
        t.left(135)
        #t.forward(self.sides[2])
    
    def area(self):
        return((1/2) * self.sides[0] * self.sides[1])

    
class circle1(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return (3.14 * self.radius * self.radius)

class Circle(circle1):
    def __init__(self,radius):
        circle1.__init__(self,radius)

    def circumference(self):
        return(2 * 3.14 * self.radius)
    
    def draw(self):
        #t = turtle.Turtle()
        t.circle(self.radius)
        #turtle.done()


class Ellipse(circle1):
    def __init__(self,radius):
        circle1.__init__(self,radius) 

    def area(self):
        return (self.radius * (self.radius/2) * 3.14 )

    def draw():
        pass


