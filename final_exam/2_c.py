from scipy import interpolate
import matplotlib.pyplot as plt
import math
import numpy as np
N=input("Enter the number of intervals : ")


def f(x):
	return(np.sqrt((r**2-x**2)))

radius=[]
area=[]
for j in range(1,11):
	r=j*5
	radius.append(r)
	a=-r
	b=r
	A=0
	h=(b-a)/float(N)
	for i in range(1,int(N)):
		x=a+(i)*h
		A=A+f(x)*h
	A=A+(h/2)*(f(a)+f(b))
	area.append(2*A)

plt.plot(radius,area,label='Original')

ans=interpolate.CubicSpline(radius,area)

plt.plot(radius,ans(radius),'r*',label='Interpolated')
plt.xlabel('Radius')
plt.ylabel('Area')
plt.legend()
plt.show()
print("Interpolated value at r=13 using library function = ",ans(13))
