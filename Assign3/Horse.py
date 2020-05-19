class Horse():
    def __init__(self):
        self.legs = 4
        self.eyes = 2
        self.color = None
        self.eat = "Anything"
        self.tail = 1
    
    def set_legs(self,legs):
        self.legs = legs
    def set_eyes(self,eyes):
        self.eyes = eyes
    def set_color(self,color):
        self.color = color
    def set_eat(self,eat):
        self.eat = eat
    def set_tail(self,tail):
        self.tail = tail
    
h = Horse()
print("Legs = ",h.legs)
print("Eyes = ",h.eyes)
print("Eat = ",h.eat)
print("Tail = ",h.eat)
h.color = "Brown"
print("Color = ",h.color)