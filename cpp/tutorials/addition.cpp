#include <iostream>

using std::cin, std::cout;

int main() {
    unsigned long long first_num{};
    unsigned long long second_num{};

    cout << "Addition" << std::endl;

    while (true) {
        cin >> first_num;
        cout << "\33[1A" << first_num << " + ";
        cin >> second_num;
        cout << "\33[1A" << first_num << " + " << second_num << " = " << first_num + second_num << std::endl;
    }

    return 0;
}