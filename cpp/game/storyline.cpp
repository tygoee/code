// This is windows-only but I still wanted to upload this old project - Dec 2022

#include <conio.h>  // _getch()

#include <iostream>
#include <string>

#define KEY_UP 72
#define KEY_DOWN 80
#define KEY_ENTER '\r'

using std::cout, std::string;

/*
 * A function to be able to choose between multiple
 * options that are highlighted when chosen.
 * You choose between the options with the arrow keys
 * with currently a maximum of 6 options.
 */
int multiChoice(
    string option1,
    string option2,
    string option3 = "",
    string option4 = "",
    string option5 = "",
    string option6 = "") {
    int selected = 1;
    bool selecting = true;
    bool justUpdated = false;

    string highl = "\033[31m";  // highlight
    string nohighl = "\033[0m";

    string options[6] = {option1, option2, option3, option4, option5, option6};

    // Calculate the amount of options
    int amountOfOptions;

    unsigned long long itemsInOptions = sizeof(options) / sizeof(options[0]);
    for (int i = 0; i <= itemsInOptions - 2; i++) {
        if (options[i] == "") {
            amountOfOptions = i;
            break;
        }
        if (i == itemsInOptions) {
            amountOfOptions = itemsInOptions;
        }
    }

    // Print the options first time
    cout << highl << option1 << nohighl << std::endl;
    for (int i = 2; i < itemsInOptions; i++) {
        cout << (amountOfOptions >= i ? options[i - 1] + "\n" : "");
    }

    // Get the keyboard inputs
    char c;
    while (selecting) {
        switch (c = _getch()) {
            case KEY_UP:
                if (selected > 1) {
                    --selected;
                    justUpdated = true;
                }
                break;
            case KEY_DOWN:
                if (selected < amountOfOptions) {
                    ++selected;
                    justUpdated = true;
                }
                break;
            case KEY_ENTER:
                selecting = false;
                break;
            default:
                break;
        }
        if (justUpdated) {
            // Goes back (amountOfOptions) lines
            cout << "\33[" + std::to_string(amountOfOptions) + "A";

            // Highlights the current selected option and reprints the lines
            for (int i = 1; i < itemsInOptions; i++) {
                if (amountOfOptions >= i) {
                    cout << (selected == i ? highl + options[i - 1] + nohighl + "\n" : options[i - 1] + "\n");
                }
            }
            justUpdated = false;
        }
    }

    // Return our selection
    return selected;
}

int main() {
    int selectedOption = multiChoice(
        "Option 1", "Option 2", "Option 3", "Option 4");
    cout << "You have selected option " << selectedOption;

    return 0;
}
