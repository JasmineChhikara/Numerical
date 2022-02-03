import numpy as np

def f(x):
	return(np.sin(np.cos(np.exp(x))))
def df(x):
	return(  -np.exp(x)   *   np.sin(np.exp(x))  *  np.cos(np.cos(np.exp(x)))        )

h=float(input("Enter tolerance : "))
x=float(input("Enter some initial x : "))


while np.abs(f(x))>h:
	x=x-(f(x)/df(x))
print("Root of equation : ",x)
