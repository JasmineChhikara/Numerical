print("Enter the interval")
a=float(input("Lower limit : "))
b=float(input("Upper limit : "))
N=input("Enter the number of intervals : ")
h=(b-a)/float(N)

def f(x):
        return(x**2)
A1=0
A2=0

for i in range(1,int(N)):
	x=a+i*h
	if i%2==0:
		A1=A1+(2*f(x)*h)
	else:
		A2=A2+(4*f(x)*h)
A=((h/3)*(f(a)+f(b)))+((A1+A2)/3)
print('Integartion value is : ',A)

