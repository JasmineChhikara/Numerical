import numpy as np
import matplotlib.pyplot as plt
x=np.loadtxt("data.txt")


plt.plot(x[:,0],x[:,1],label='Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title(' y vs x')
plt.legend()
plt.show()
