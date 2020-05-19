class Elephant():
    def __init__(self):
        self.trunk = 1
        self.legs = 4
        self.eyes = 2
        self.eat = "Anything"
        self.color = None

    def get_trunk(self):
        return self.trunk
    def get_legs(self):
        return self.legs
    def get_eyes(self):
        return self.eyes
    def get_eat(self):
        return self.eat
    def get_color(self):
        return self.color
    
e = Elephant()
print("Trunk = ", e.get_trunk())
print("Legs = ",e.get_legs())
print("Eyes = ",e.get_eyes())
print("Eat = ",e.get_eat())
e.color = "Grey"
print("Color = ",e.get_color())