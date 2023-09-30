// This is windows-only but I still wanted to upload this old project - Dec 2022. I used
// https://stackoverflow.com/questions/24708700/c-detect-when-user-presses-arrow-key

#include <conio.h>  // For _getch()

#include <iostream>

#define KEY_UP 72
#define KEY_DOWN 80
#define KEY_ENTER '\r'

int main() {
    // Variables
    int selected = 0;
    int numChoices = 3;
    bool selecting = true;
    bool updated = false;

    // Output options
    std::cout << "A. Option 1\n";
    std::cout << "B. Option 2\n";
    std::cout << "C. Option 3\n";

    // Executes actions when pressing keys
    char c;
    while (selecting) {
        switch (c = _getch()) {
            case KEY_UP:
                if (selected > 0) {
                    --selected;
                    updated = true;
                }
                break;
            case KEY_DOWN:
                if (selected < numChoices - 1) {
                    ++selected;
                    updated = true;
                }
                break;
            case KEY_ENTER:
                selecting = false;
                break;
            default:
                break;
        }
        if (updated) {
            std::cout << "Option " << (selected + 1) << " is selected.\n";
            updated = false;
        }
    }
    // Lets us know what we ended up selecting.
    std::cout << "Selected " << (selected + 1) << '\n';

    return 0;
}