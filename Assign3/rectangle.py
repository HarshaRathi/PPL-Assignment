import turtle

class rectangle():
	def __init__(self,a = 5,b = 5):
		self.__side1 = a
		self.__side2 = b

	def get_side1(self):
		return self.__side1
	def get_side2(self):
		return self.__side2

	def find_area(self):
		return (self.__side1 * self.__side2)

	def find_perimeter(self):
		return(2 * self.__side1 + 2 * self.__side2)

	def draw(self):
		t = turtle.Turtle()
		t.forward(self.__side1)
		t.left(90)
		t.forward(self.__side2)
		t.left(90)
		t.forward(self.__side1)
		t.left(90)
		t.forward(self.__side2)
		t.left(90)
		turtle.done()


s = rectangle(200,100)
print("Length of the side1 of rectangle is ",s.get_side1(),"cm")
print("Length of the side2 of rectangle is ",s.get_side2(),"cm")
print("Area of rectangle is ",s.find_area(),"sq.cm")
print("Perimeter of rectangle is",s.find_perimeter(),"cm")
s.draw()
