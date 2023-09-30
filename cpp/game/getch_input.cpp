#include <conio.h>

#include <iostream>
#include <string>
using std::cout;

#define KEY_UP 72     // P
#define KEY_DOWN 80   // H
#define KEY_LEFT 75   // K
#define KEY_RIGHT 77  // M
#define KEY_TAB '\t'
#define KEY_ENTER '\r'

int main() {
    const char ascii[53] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    bool busy = true;

    unsigned long long itemsInAscii = sizeof(ascii) / sizeof(ascii[0]);
    for (int i = 0; i < itemsInAscii; ++i) {
        // cout << ascii[i];
    }

    char ch;
    while (busy) {
        // clang-format off
        switch (ch = _getch()) {
            case KEY_UP: cout << "up"; break;
            case KEY_DOWN: cout << "down"; break;
            case KEY_LEFT: cout << "left"; break;
            case KEY_RIGHT: cout << "right"; break;
            case KEY_TAB: cout << "tab"; break;
            case KEY_ENTER: cout << "enter"; busy = false; break;
            // clang-format on
            default:
                cout << ch;
                for (int i = 0; i < itemsInAscii; ++i) {
                    if (ch == ascii[i]) {  // if ch is in ascii
                        cout << "\n"
                             << ascii[i];
                    }
                }
                break;
        }
    }

    return 0;
}