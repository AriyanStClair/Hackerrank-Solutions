# Reverse he order of the input array

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,temp,arr[1000]; //input array
    cin>>n;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    for(int i = 0; i < n/2; i++){ //swap elements to reverse order
        temp = arr[i];
        arr[i] = arr[n-1-i];
        arr[n-1-i] = temp;
    }
    
    for(int i = 0; i < n; i++){
         cout<<arr[i]<<' ';
     }
    
    
    return 0;
}
