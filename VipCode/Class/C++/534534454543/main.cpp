#include <iostream>

using namespace std;

int main()
{
    cout<<"ÇëÊäÈëÊý×Ö: ";
    int a, b=10, c=1;
    cin>>a;
    while(1)
    {
        if(a<b)
        {
            cout<<c;
            break;
        }
        c++;
        b*=10;
    }
    return 0;
}
