import numpy as np


print("Enter the interval")
a=float(input("Lower value : "))
b=float(input("Upper value : "))


#function 
def f(x):
	return(np.sin(np.cos(np.exp(x))))


x_m=float(0.5*(a+b))
h=float(input("Enter tolerance : "))


while np.abs(f(x_m))>h:
	if f(a)*f(x_m)>0:
		a=x_m
	elif f(a)*f(x_m)<0:
		b=x_m
	x_m=(a+b)*0.5
print("Root of equation is : ",x_m)
