#include <iostream>
#include <string>

using namespace std;

int main() {
    string name = 0;
    int age;

    cout << "[Intercom] J. Miller to the captains" << endl;
    cin >> name;
    cout << "Hello I'm " << name << endl;

    cout << "What is your age? ";
    cin >> age;
    cout << "My age is " << age << endl;

    return 0;
}