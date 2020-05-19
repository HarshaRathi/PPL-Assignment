class dog():
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__tail = 1
        self.__color = None
        self.__eat = "Anything"
    def get_legs(self):
        return(self.__legs)
    def get_eyes(self):
        return(self.__eyes)
    def get_tail(self):
        return(self.__tail)
    def get_color(self):
        return(self.__color)
    def set_legs(self,legs):
        self.__legs = legs
    def set_eyes(self,eyes):
        self.__eyes = eyes
    def set_tail(self,tail):
        self.__tail = tail
    def set_color(self,color):
        self.__color = color
    def set_eat(self,eat):
        self.__eat = eat
    def get_eat(self):
        return self.__eat
    
d = dog()
print("Legs = ",d.get_legs())
d.set_legs(3)
print("Legs = ",d.get_legs())
print("Eyes = ",d.get_eyes())
d.set_eyes(2)
print("Eyes = ",d.get_eyes())
print("Tail = ",d.get_legs())
print("color = ",d.get_color())
d.set_color("Black")
print("color=",d.get_color())
print("Enter what dog eats")
eats = list(input().split())
d.set_eat(eats)
print("Dog eat = ",d.get_eat())