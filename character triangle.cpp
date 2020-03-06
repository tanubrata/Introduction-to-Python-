//Name: Tanubrata Dey
//Date: 2 May 2018
//My C++ program draws Character graphics triangle

#include <iostream>
using namespace std;

int main()
{

    int i,j,size;
    cout << "Enter a size: ";
    cin >> size;
    
    for (i = size; i > 0 ; i--)
    {
        for (j = 0; j < i; j++)
            cout << "*";
        cout << endl;
    }
    return 0;
}
