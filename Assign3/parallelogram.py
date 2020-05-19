import turtle
class parallelogram():
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def perimeter(self):
        return(2*(self.__a+self.__b))
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.__a)
        t.left(135)
        t.forward(self.__b)
        t.left(45)
        t.forward(self.__a)
        t.left(135)
        t.forward(self.__b)
        turtle.done()
print("Enter the length of side")
l = list(map(int,input().split()))
p = parallelogram(l[0],l[1])
print("perimeter of parallelogram = ",p.perimeter())
p.draw()    