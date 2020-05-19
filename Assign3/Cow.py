class Cow():
    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.tail = 1
        self.color = None
        self.eat = "Anything"
        self.horn = 2

    def get_legs(self):
        return(self.legs)
    def get_eyes(self):
        return(self.eyes)
    def get_tail(self):
        return(self.tail)
    def get_color(self):
        return(self.color)
    def set_legs(self,legs):
        self.legs = legs
    def set_eyes(self,eyes):
        self.eyes = eyes
    def set_tail(self,tail):
        self.tail = tail
    def set_color(self,color):
        self.color = color
    def set_eat(self,eat):
        self.eat = eat
    def get_eat(self):
        return self.eat
    def set_horn(self,horn):
        self.horn = horn

c = Cow()
print("Legs = ", c.get_legs())
print("Eyes = ",c.get_eyes())
print("Tail = ",c.get_tail())
#print("Color = ",c.get_color())
c.set_color("White")
print("Color = ",c.get_color())
c.set_eat("Grass")
print("Eat = ",c.get_eat())
