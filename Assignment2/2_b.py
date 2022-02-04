import numpy as np




print("Enter the interval")
a=float(input("Lower limit : "))
b=float(input("Upper limit : "))
N=input("Enter the number of intervals : ")
h=(b-a)/float(N)

def f(x):
        return(np.exp(x))

At=0
A1s=0
A2s=0

for i in range(1,int(N)):
	x=a+(i)*h
	At=At+f(x)*h
	if i%2==0:
		A1s=A1s+(2*f(x)*h)
	else:
		A2s=A2s+(4*f(x)*h)


At=At+(h/2)*(f(a)+f(b))
As=((h/3)*(f(a)+f(b)))+((A1s+A2s)/3)
print("Integration valueu using trapezoidal rule : ",At)
print("Integration valueu using Simpson rule : ",As)










