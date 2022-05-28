#include <iostream>

using namespace std;
int n=0;
int add_num(int s)
{
    n+=s;
    if(s == 1)
    {
        return 1;
    }
    else
    {
        return add_num(s-1)+1;
    }


}

int main()
{
   int m;
   cin>>m;
   add_num(m);
   cout<<n;
   return 0;
}
