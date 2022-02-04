import numpy as np
import matplotlib.pyplot as plt



#using bisection
print("Enter the interval for bisection")
a1=float(input("Lower value : "))
b1=float(input("Upper value : "))
h=float(input("Enter tolerance : "))
x=float(input("Enter initial point for newton raphson : "))





def f(x):
	return(np.sin(np.cos(np.exp(x))))
def df(x):
        return(  -np.exp(x)   *   np.sin(np.exp(x))  *  np.cos(np.cos(np.exp(x)))        )






x_m=float(0.5*(a1+b1))
bis=[]
new=[]



for j in range(0,10):
	a=a1
	b=b1
	for i in range(j):
		if f(a)*f(x_m)>0:
			a=x_m
		elif f(a)*f(x_m)<0:
			b=x_m
		x_m=(a+b)*0.5
		x=x-(f(x)/df(x))
	bis.append(x_m)
	new.append(x)







it=[]
erbis=[]
ernew=[]
for k in range(len(new)-1):
	it.append(k)
	erbis.append(bis[k+1]-bis[k])
	ernew.append(new[k+1]-new[k])
plt.plot(it,erbis,label='Bisection')
plt.plot(it,ernew,label='Newton raphson')

plt.xlabel('Number of Iterations')
plt.ylabel('Error')
plt.title('Error vs Iterations for Bisection and Newton Raphson method')
plt.legend(['Bisection Method','Newton Raphson'])
plt.show()









i
