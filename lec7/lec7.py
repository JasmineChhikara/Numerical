import numpy as np
def f(x):
	return(x**2-10)
def df(x):
	return(2*x)
x=float(input("Enter initial point"))
for i in range(100):
	x=x-(f(x)/df(x))
print(x)
