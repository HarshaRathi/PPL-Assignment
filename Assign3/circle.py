import turtle

class circle1():
	def __init__(self,a = 5):
		self.__radius = a

	def get_radius(self):
		return self.__radius
	
	def find_area(self):
		area = 3.14 * (self.__radius * self.__radius)
		return area
		

	def find_circumference(self):
		circum = 2 * 3.14 * self.__radius
		return circum
		
	def draw(self):
		t = turtle.Turtle()
		t.circle(self.__radius)	
		turtle.done()

c = circle1(20)
print("Radius of a circle is ", c.get_radius())
print("Area of a circle is ",c.find_area())
print("Circumference of a circle is ",c.find_circumference())
c.draw()


	
