class Rabbit():
    def __init__(self):
        self.eyes = 2
        self.eat = "Anything"
        self.ear = 2
        self.legs = 4
        self.color = None
    
    def get_eyes(self):
        return self.eyes
    def set_eyes(self,eye):
        self.eyes = eye
    def get_ear(self):
        return self.ear
    def set_ear(self,ear):
        self.ear = ear
    def get_leg(self):
        return self.legs
    def set_leg(self,leg):
        self.legs = leg
    def set_eat(self,eat):
        self.eat = eat
    def get_eat(self):
        return self.eat
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color

r = Rabbit()
print("Legs = ",r.legs)
print("Eyes = ",r.eyes)
print("Ear = ",r.ear)
r.eat = "Carrot"
print("Eat = ",r.eat)
r.color = "White"
print("Color = ",r.color)