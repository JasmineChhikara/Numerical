

print("Enter the interval")
a=float(input("Lower limit : "))
b=float(input("Upper limit : "))
N=input("Enter the number of intervals : ")
h=(b-a)/float(N)

def f(x):
	return(x**2)
A=0

for i in range(0,int(N)):
	x=a+i*h
	A=A+f(x)*h
print(x)
print("Integration value : ",A)	
