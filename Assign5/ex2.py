import sys
class DivideByZeroError(Exception): 
  def __init__(self, value): 
        self.value = value 
  def __str__(self): 
        return(repr(self.value)) 


a = int(input("Enter the Value of a"))
b = int(input("Enter the value of b"))
try:
    if b == 0:
        raise(DivideByZeroError("Divide By Zero"))
    print("Result is",a/b)
    
except DivideByZeroError as error:
    print("Error: ",error.value)
except:
    print("Unexpected error:", sys.exc_info()[0])

