import numpy as np

def Square(a):
	return(a**2)
a=float(input("Enter the number : "))
print("Square of number =",Square(a))

b=np.array([1,3,5])
print("Square of a list:",Square(b))
