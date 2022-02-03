import numpy as np
from scipy import optimize

def f(x):
	return(np.sin(np.cos(np.exp(x))))
def df(x):
	return(  -np.exp(x)   *   np.sin(np.exp(x))  *  np.cos(np.cos(np.exp(x)))        )
a=float(input("Enter lower limit : "))
b=float(input("Enter upper limit : "))
bis=optimize.bisect(f,a,b)
print(bis)
