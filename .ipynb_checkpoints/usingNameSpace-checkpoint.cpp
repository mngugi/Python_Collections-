/*Use the namespace keyword to simplify typing*/

#include <iostream>
using namespace std;

int main()
{
    int variableName = 23;
    std::cout << "Hey, writing std:: is pain, ";
    std::cout << "change the program so I don't have to write it."<<"\n";
    std:: cout << "Integer value:"<<variableName;
    return 0;
}
