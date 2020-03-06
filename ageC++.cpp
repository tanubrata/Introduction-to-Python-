//Name: Tanubrata Dey
//Date: 3 May 2018
//This C++ program asks user for Age

#include <iostream>
using namespace std;

int main()
{
    int num;
    cout << "Enter an age in positive number: ";
    cin >> num;
    
    while (num <= -1){
        cout << "Entered a negative number" << endl;
        cout << "Enter an age in positive number: ";
        cin >> num;
        
    }
    
    cout << "You entered your age as: " << num << endl;
    
    return 0;
}
