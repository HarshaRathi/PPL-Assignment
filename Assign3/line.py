import turtle
class line():
    def __init__(self , len = 5):
        self.__len = len
    
    def get_len(self):
        return self.__len
    
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.__len)

l = line(400)
print("Length of line = ",l.get_len())
l.draw()
turtle.done()