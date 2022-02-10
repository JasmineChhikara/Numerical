import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


x1=np.loadtxt("data.txt")
x=x1[:,0]
y=x1[:,1]
ans=interpolate.CubicSpline(x,y)
#plt.plot(x1[:,0],x1[:,1],label="Original data points")
plt.plot(x,ans(x),label='Interpolated')
plt.xlabel('x')
plt.ylabel('y')
plt.title(' y vs x')
plt.legend()
plt.show()
