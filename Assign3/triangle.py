import turtle
import math
class triangle():
	def __init__(self,a = 5 ,b = 5, c = 5):
		self.__side1 = a
		self.__side2 = b
		self.__side3 = c

	def get_side1(self):
		return self.__side1
	
	def get_side2(self):
		return self.__side2

	def get_side3(self):
		return self.__side3

	def find_perimeter(self):
		return(self.__side1 + self.__side2 + self.__side3)

tr = triangle(10,20,30)
print("Length of the side1 of triangle = ",tr.get_side1())
print("Length of the side2 of triangle = ",tr.get_side2())
print("Length of the side3 of triangle = ",tr.get_side3())
print("Perimeter of the triangle = ",tr.find_perimeter(),"cm")

	
	
	
	
