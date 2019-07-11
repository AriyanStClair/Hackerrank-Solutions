#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    int integer;
    long int_long;
    char c;
    float f;
    double d;

    cin>>integer>>int_long>>c>>f>>d;
    cout<<integer<<'\n'<<int_long<<'\n'<<c<<'\n'<<setprecision(3)<<fixed<<f<<'\n'<<
    setprecision(9)<<fixed<<d;         
    return 0;
}
