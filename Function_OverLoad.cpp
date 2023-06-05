#include <iostream>
#include <cstdlib>

using namespace std;

int abs(int t);
double abs(double d);

int main() {
    cout << abs(-10) << "\n";
    //cout << abs(-11.0) << "\n";
    cout << labs(-9L)  << "\n";

    return 0;
}

int abs(int i) {
    cout << "Using Integer abs() \n";
    return i < 0 ? -i : i;
}

double abs(double d) {
    cout << "Using double abs() \n";
    return d < 0.0 ? -d : d;
}
