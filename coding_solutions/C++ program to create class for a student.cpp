/*
C++ program to create class for a student.
*/
#include <iostream>
using namespace std;

class student
{
	private:
		char  name[30];
		int   rollNo;
		
	public:
		
		void getDetails(void);
		
		void putDetails(void);
};

//member function definition, outside of the class
void student::getDetails(void){
	cout << "Enter name: " ;
	cin >> name;
	cout << "Enter roll number: ";
	cin >> rollNo;
	
}


void student::putDetails(void){
	cout << "Student details:\n";
	cout << "Name:"<< name << ",Roll Number:" << rollNo ;
}

int main()
{
	student std;		//object creation
	
	std.getDetails();
	std.putDetails();
	
	return 0;
