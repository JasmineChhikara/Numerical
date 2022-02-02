#include<iostream>
using namespace std;

int main()
{
	int arr[5]={1,3,5,6,2};
	cout<<sizeof(arr[0])<<endl;
	cout<<sizeof(arr)<<endl;
	int len=sizeof(arr)/sizeof(arr[0]);
	cout<<len<<endl;
	for (int i=0;i<5;i++)
	{
		if(i!=3)
		{
			cout<<arr[i]<<endl;
		}
	}
	int sum=0;
	int j=0;
	while(sum<12)
	{
		cout<<arr[j]<<endl;
		sum+=arr[j];
		j++;
	}
}
