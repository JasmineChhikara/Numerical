import numpy as np
def f(x,y):
	return np.sqrt(4-(x**2)-(y**2))


xi=-1.0
xf=1.0
yi=-1.0
yf=1.0
n_x=float(input("Enter number of intervals for x "))
n_y=float(input("Enter number of intevals for y "))

h_x=(xf-xi)/n_x
h_y=(yf-yi)/n_y
I=0.0
for i in range(int(n_x-2)):
    for j in range(int(n_y-2)):
        x=xi+(h_x/2)+i*h_x
        y=yi+(h_y/2)+j*h_y
        I=I+ (h_x*h_y*f(x,y))
print("Integration value is",I)
