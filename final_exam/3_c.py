import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


x1=np.loadtxt("data.txt")
x=x1[:,0]
y=x1[:,1]
f=interpolate.CubicSpline(x,y)

print("Enter the interval")
a=float(input("Lower value : "))
b=float(input("Upper value : "))



x_m=float(0.5*(a+b))
h=float(input("Enter tolerance : "))


while np.abs(f(x_m))>h:
	if f(a)*f(x_m)>0:
		a=x_m
	elif f(a)*f(x_m)<0:
		b=x_m
	x_m=(a+b)*0.5
print("Root of equation is : ",x_m)

