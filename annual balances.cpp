//Name: Tanubrata Dey
//Date: 7 May 2018
//My C++ program prints: Annual Balances

#include<iostream>
using namespace std;

int main()
{
    double principal;
    float rate = 1.1;
    
    int years;
    cout << "Enter an amount: ";
    cin >> principal;
    
    
    for (years = 1; years <= 5; years++) {
        principal = principal * rate;
        
      
        
        cout <<years << "\t\t" << principal << endl;
    }
    
    return 0;
}
