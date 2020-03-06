//Name: Tanubrata Dey
//Date: 2 May 2018
//My C++ program converts km to miles

#include <iostream>
using namespace std;

int main()
{
    float km, miles;
    cout << "Enter a distance in km: ";
    cin >> km;
    miles = 0.621371 * km;
    cout << "miles:" << miles << endl;
    return 0;
}
