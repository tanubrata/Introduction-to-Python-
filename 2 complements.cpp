//Name: Tanubrata Dey
//Date: 3 May 2018
//My C++ program prints 2 complements

#include <iostream>
using namespace std;

int main() {
    
    int n, x = 0, b;
    cout << " Enter a number: ";
    cin >> n;
    
    if (n <= -1){
        cout << "1";
        x = 32 + n;
    }
    
    else if (n >= 0){
        cout << "0" ;
        x = n;
    }
    
    b = 16;
                 
    while (b > 0.5){
        
        if (x >= b)
            cout << 1;
        else
            cout << 0;
        
        x = (x % b);
        
        b = (b / 2);
    }
    cout << "\n";
    
    return 0;
    
    
}
