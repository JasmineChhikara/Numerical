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

print(radius)
print(area)

plt.plot(radius,area)
plt.xlabel('Radius')
plt.ylabel('Area')
plt.title('Change of area with radius')
plt.show()


