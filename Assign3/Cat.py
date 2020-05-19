class Cat():
    def __init__(self):
        self.__legs = 4
        self.__eyes = 2
        self.__tail = 1
        self.__eat =  "Anything"
        self.__color = None

    def set_leg(self,leg):
        self.__legs = leg
    def get_leg(self):
        return self.__legs

    def set_eyes(self,eyes):
        self.__eyes = eyes
    def get_eyes(self):
        return self.__eyes

    def set_tail(self,tail):
        self.__tail = tail
    def get_tail(self):
        return self.__tail

    def set_eat(self,eat):
        self.__eat = eat
    def get_eat(self):
        return self.__eat

    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color

c = Cat()
print("Legs = " ,c.get_leg())
print("Eyes = " ,c.get_eyes())
print("Tail = " ,c.get_tail())
c.set_eat("Drinks Milk")
print("Eat/Drink = " ,c.get_eat()) 
c.set_color("Brown")
print("Color = " ,c.get_color())