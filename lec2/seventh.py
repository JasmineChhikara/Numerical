import numpy as np
arr_list=[1,3,5,6,2] //this is a list
arr=np.array(arr_list)  //here we convert things to array
for i in range(len(arr)):
	if i!=3:
		print(arr[i])
sum=0
j=0
while sum<12:
	print(arr[j])
	sum+=arr[j]
	j+=1
