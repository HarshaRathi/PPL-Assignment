class Deer():
    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.eat = "Anything"
        self.color = None
        self.horn = 2

    def get_legs(self):
        return self.legs 
    def set_legs(self,l):
        self.legs = l
    def get_eyes(self):
        return self.eyes
    def set_eyes(self,e):
        self.eyes = e
    def get_horn(self):
        return self.horn
    def set_horn(self,horn):
        self.horn = horn
    def get_color(self):
        return self.color
    def set_color(self,c):
        self.color = c
    def set_eat(self,e):
        self.eat = e
    def get_eat(self):
        return self.eat

d = Deer()
print("Legs = ",d.get_legs())
print("Eyes = ",d.get_eyes())
print("Horn = ",d.get_horn())
print("Color = ",d.get_color())
print("Eat = ",d.get_eat())