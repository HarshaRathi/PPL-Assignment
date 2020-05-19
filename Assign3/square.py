import turtle

class square():
	def __init__(self,a = 5):
		self.__side = a

	def get_side(self):
		return self.__side

	def find_area(self):
		return (self.__side * self.__side)

	def find_perimeter(self):
		return(4 * self.__side)

	def draw(self):
		t = turtle.Turtle()
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		turtle.done()


s = square(200)
print("Length of the side of square is ",s.get_side(),"cm")
print("Area of square is ",s.find_area(),"sq.cm")
print("Perimeter of square is",s.find_perimeter(),"cm")
s.draw()
