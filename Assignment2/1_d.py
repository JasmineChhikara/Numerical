import numpy as np
from scipy import optimize

def f(x):
	return(np.sin(np.cos(np.exp(x))))
def df(x):
	return(  -np.exp(x)   *   np.sin(np.exp(x))  *  np.cos(np.cos(np.exp(x)))        )
a=float(input("Enter lower limit for bisection : "))
b=float(input("Enter upper limit for bisection : "))
c=float(input("Enter bound for newton raphson : "))
bis=optimize.bisect(f,a,b)
new=optimize.newton(f,c,df)
print('Ans for bisection',bis)
print('Ans for newton raphson',new)





