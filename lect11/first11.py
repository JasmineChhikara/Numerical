import numpy as np
from scipy import interpolate

x=[0,1,2]
y=[1,2,4]
ans=interpolate.CubicSpline(x,y)
print("Interpolated value at x=1.5 using library function = ",ans(1.5))
print("2^(1.5) = ",2**(1.5))
print("Error =:",2**(1.5)-ans(1.5))
