import numpy as np
import matplotlib.pyplot as plt



#using bisection
print("Enter the interval")
a=float(input("Lower value : "))
b=float(input("Upper value : "))


def f(x):
	return(np.sin(np.cos(np.exp(x))))


x_m=float(0.5*(a+b))
h=float(input("Enter tolerance : "))


bis=[]

for j in range(0,10):
	a=-1
	b=1
	for i in range(j):
		if f(a)*f(x_m)>0:
			a=x_m
		elif f(a)*f(x_m)<0:
			b=x_m
		x_m=(a+b)*0.5
	bis.append(x_m)
print(bis)





#using newton rapson
def f(x):
	return(np.sin(np.cos(np.exp(x))))
def df(x):
	return(  -np.exp(x)   *   np.sin(np.exp(x))  *  np.cos(np.cos(np.exp(x)))        )

x=float(input("Enter initial point : "))

new=[]
for j in range(0,10):
	for i in range(j):
		x=x-(f(x)/df(x))
	new.append(x)








it=[]
erbis=[]
ernew=[]
for k in range(len(new)-1):
	it.append(k)
	erbis.append(bis[k+1]-bis[k])
	ernew.append(new[k+1]-new[k])
plt.plot(it,erbis,label='Bisection')
#plt.plot(it,ernew,label='Newton raphson')

plt.xlabel('Number of Iterations')
plt.ylabel('Error')
plt.title('Error vs Iterations for Bisection and Newton Raphson method')
#plt.legend(['Bisection Method','Newton Raphson'])
plt.show()









i
