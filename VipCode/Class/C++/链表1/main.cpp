#include <iostream>

using namespace std;

int main()
{
    struct student
    {
        char name[20];
        int age;
        student* next;
    }  ;
    student c= {"Kaka",23,NULL};
    student b= {"Deco",27,&c};
    student a= {"Terry",30,&b};
    student* head=&a;
    student* pointer=head;
    cout<<"Head->";
    while(pointer)
    {
        cout<<(*pointer).name<<"->"<<(*pointer).age<<"->";
        pointer=(*pointer).next;

    }
    cout<<"End"<<endl;

    return 0;
}
