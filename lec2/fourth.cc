#include<iostream>
using namespace std;
int main()
{
	char name[1];
	cout << "Please enter name: ";
	cin >> name;
	cout << "entered name: " << name << endl;
	float a;
	cout << "Please enter a number: ";
	cin >> a;
	a *=a;
	cout << "Square of the number: " << a << endl;
}
