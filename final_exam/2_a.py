import math
import numpy as np
print("Enter the interval")
a=float(input("Lower limit (negative radius value) : "))
b=float(input("Upper limit (radius value): "))
N=input("Enter the number of intervals : ")
h=(b-a)/float(N)
r=float(input("Enter the radius : "))

def f(x):
	return(np.sqrt((r**2-x**2)))
A=0

for i in range(1,int(N)):
	x=a+(i)*h
	A=A+f(x)*h
A=A+(h/2)*(f(a)+f(b))
print("Area of circle : ",2*A)







