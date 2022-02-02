import numpy as np
arr=[1,3,'a','b',5,'4',6,2]
print(arr[3])
print(arr[-1])
print(arr[-2])
print(arr[:3])
print(arr[1:-1])
print(arr[3:])

new_arr=[]

for i in arr:
	if isinstance(i,int):
		new_arr.append(i)
print(new_arr)
arr_arr=np.array(new_arr)
