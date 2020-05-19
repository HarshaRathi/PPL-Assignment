class Tiger():
    def __init__(self):
        self.legs =  4
        self.eyes =  2
        self.tail =  1
        self.color = "Many Colors"
        self.eat = "Anything"

    def set_legs(self,legs):
        self.legs = legs
    def get_legs(self):
        return self.legs
    def set_eyes(self,eyes):
        self.eyes = eyes
    def get_eyes(self):
        return self.eyes
    def set_tail(self,tail):
        self.tail = tail
    def get_tail(self):
        return self.tail
    def set_color(self,color):
        self.color = color 
    def get_color(self):
        return self.color
    def set_eat(self,eat):
        self.eat = eat
    def get_eat(self):
        return self.eat

t = Tiger()
print("Legs = ", t.get_legs())
print("Eyes = ", t.get_eyes())
print("Tail = ", t.get_tail())
print("Eat = ", t.get_eat())
t.set_color("White orange n black strips")
print("Color = ",t.get_color())