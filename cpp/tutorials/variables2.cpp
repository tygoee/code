#include <ctime>
#include <iostream>

using namespace std;

int main() {
    int decimal = 255;
    int binary = 0b11111111;
    int hexadecimal = 0xff;

    int number = 1'000'000;
    short another = number;
    cout << another << endl;  // 16960

    return 0;
}