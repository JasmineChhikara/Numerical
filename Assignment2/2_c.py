import numpy as np
import matplotlib.pyplot as plt



print("Enter the interval")
a=float(input("Lower limit : "))
b=float(input("Upper limit : "))
N=int(input("Enter the interval : "))

def f(x):
	return(np.exp(x))

it1,it2=[],[]
left,right,mid,trap,simp=[],[],[],[],[]
errl,errr,errm,errt,errs=[],[],[],[],[]



for j in range(1,N):
	Al,Am,Ar=0,0,0
	h=(b-a)/(j)
	for i in range(j):
		xl=a+i*h
		Al=Al+f(xl)*h
		xr=a+(i+1)*h
		Ar=Ar+f(xr)*h
		xm=a+(i+0.5)*h
		Am=Am+f(xm)*h
	left.append(Al)
	right.append(Ar)
	mid.append(Am)



for t in range(1,N):
	At,A1s,A2s=0,0,0
	h=(b-a)/t
	for i in range(1,t):
		x=a+i*h
		At=At+f(x)*h
		if i%2==0:
			A1s=A1s+(2*f(x)*h)
		else:
			A2s=A2s+(4*f(x)*h)
	At=At+(h/2)*(f(a)+f(b))
	As=((h/3)*(f(a)+f(b)))+((A1s+A2s)/3)
	trap.append(At)
	if t%2==0:
		simp.append(As)



for k in range(1,N-1):
	it1.append(k)
	errl.append(left[k]-left[k-1])
	errr.append(right[k]-right[k-1])
	errm.append(mid[k]-mid[k-1])
	errt.append(trap[k]-trap[k-1])

for z in range(1,len(simp)-1):
	it2.append(2*(z))
	errs.append(simp[z]-simp[z-1])




plt.plot(it1,errl,label="Left point")
plt.plot(it1,errr,label="Right point")
plt.plot(it1,errm,label="Mid point")
plt.plot(it1,errt,label="Trapezoidal")
plt.plot(it2,errs,label="Simpson")
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.title("Error vs iterations")
plt.legend()
plt.show()









