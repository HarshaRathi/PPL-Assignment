class Fish():
    def __init__(self):
        self.eat = "Anything"
        self.color = None
        self.blooded = "Cold Blooded"
        self.type = None
        self.fintype = None
    
    def get_eat(self):
        return self.eat
    def get_color(self):
        return self.color
    def get_blooded(self):
        return self.blooded
    def get_type(self):
        return self.type
    def get_fintype(self):
        return self.fintype

    def set_eat(self,eat):
        self.eat = eat
    def set_color(self,color):
        self.color = color
    def set_blooded(self,blooded):
        self.blooded = blooded
    def set_type(self,type):
        self.type = type
    def set_fintype(self,fintype):
        self.fintype=fintype

F = Fish()
F.eat = "Frozen Food"
F.color = "Multicolor"
F.blooded = "Cold Blooded"
F.type = "Cat Fish"
F.fintype = "Anal Fins"
print("Eat = ",F.eat)
print("Color = ",F.color)
print("Blooded = ",F.blooded)
print("Type of Fish = ",F.type)
print("Fintype of Fish = ",F.fintype)