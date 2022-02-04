import numpy as np


print("Enter the interval")
a=float(input("Lower limit : "))
b=float(input("Upper limit : "))
N=input("Enter the number of intervals : ")
h=(b-a)/float(N)

def f(x):
	return(np.exp(x))
Al=0
Ar=0
Am=0

for i in range(0,int(N)):
	xl=a+i*h
	Al=Al+f(xl)*h
	xr=a+(i+1)*h
	Ar=Ar+f(xr)*h
	xm=a+(i+0.5)*h
	Am=Am+f(xm)*h



print("Integration value using left point rule : ",Al)
print("Integration value using right point rule : ",Ar)
print("Integration value using mid point rule : ",Am)

# Mid point rule gives best value. Checked the result


	
