from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,eat,color,eyes):
        self.eat = eat
        self.color = color
        self.eyes = eyes
    
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color

    def get_eat(self):
        return self.eat
    def set_eat(self,eat):
        self.eat = eat

    def get_eyes(self):
        return self.eyes
    def set_eyes(self,eyes):
        self.eyes = eyes

    @abstractmethod
    def gettype(self):
        pass
   


class SAnimal(Animal):
    def __init__(self,eat,color,eyes,legs,tail):
        Animal.__init__(self,eat,color,eyes)
        self.legs = legs
        self.tail = tail

    def get_tail(self):
        return self.tail
    def set_tail(self):
        self.tail = tail

    def get_legs(self):
        return self.legs
    def set_legs(self):
        self.legs = legs
    def gettype(self):
        print("Surface Animal")

class Dog(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
    
class Cat(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)

class Deer(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail,horn):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
        self.horn = horn
    
    def get_horn(self):
        return self.horn
    def set_horn(self):
        self.horn = horn

class Rabbit(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail,use):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
        self.use = use
    
    def get_use(self):
        return self.use
    def set_use(self,use):
        self.use = use
    

class Cow(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail,give):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
        self.give = give

    def set_give(self,give):
        self.give = give
    def get_give(self):
        return self.give

    

class Elephant(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail,trunk):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
        self.trunk = trunk

    def get_trunk(self):
        return self.trunk
    def set_trunk(self,trunk):
        self.trunk = trunk

class Horse(SAnimal):
    def __init__(self,eat,color,eyes,legs,tail,use):
        SAnimal.__init__(self,eat,color,eyes,legs,tail)
        self.use = use
    
    def get_use(self):
        return self.use
    def set_use(self):
        self.use = use

class WAnimal(Animal):
    def __init__(self,eat,color,eyes,blooded,swim):
        Animal.__init__(self,eat,color,eyes)
        self.blooded = blooded
        self.swim = swim

    def set_blooded(self,blooded):
        self.blooded = blooded
    def get_blooded(self):
        return self.blooded

    def set_swim(self,swim):
        self.swim = swim
    def get_swim(self):
        return self.swim
    def gettype(self):
        print("Water Bodies")

class Fish(WAnimal):
    def __init__(self,eat,color,eyes,blooded,swim,type,fintype):
        WAnimal. __init__(self,eat,color,eyes,blooded,swim)
        self.type = type
        self.fintype = fintype

    def set_type(self,type):
        self.type = type
    def get_type(self):
        return self.type

    def set_fintype(self,fintype):
        self.fintype = fintype
    def get_fintype(self):
        return self.fintype

class Dolphin(WAnimal):
    def __init__(self,eat,color,eyes,blooded,swim,fintype,teeth):
        WAnimal. __init__(self,eat,color,eyes,blooded,swim)
        self.fintype = fintype
        self.teeth = teeth

    def set_teeth(self,teeth):
        self.teeth = teeth
    def get_teeth(self):
        return self.teeth

    def set_fintype(self,fintype):
        self.fintype = fintype
    def get_fintype(self):
        return self.fintype

class Octopus(WAnimal):
    def __init__(self,eat,color,eyes,blooded,swim,arms):
        WAnimal. __init__(self,eat,color,eyes,blooded,swim)
        self.arms = arms

    def set_arms(self,arms):
        self.arms = arms
    def get_arms(self):
        return self.arms


