#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string numbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight",      "nine"};
    if (n > 9){
        printf("Greater than 9");
    }

    else{
        cout<<numbers[n-1];
    }


    return 0;
}
