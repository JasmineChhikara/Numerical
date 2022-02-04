import numpy as np
from scipy import integrate
a=float(input("Enter lower limit : "))
b=float(input("Enter upper limit : "))

def f(x):
	return(np.exp(x))


x=np.linspace(a,b,100)
At=np.trapz(f(x),x)
As=integrate.simpson(f(x),x)
Ar=integrate.romberg(f,a,b)
Afq=integrate.fixed_quad(f,a,b)

print("Using trapezoidal rule : ",At)
print("Using Simpson rule : ",As)
print("Using Romberg rule : ",Ar)
print("Using Gaussian Quadrature : ",Afq)






