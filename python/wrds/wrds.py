# I made this in april 2023, and modified it a bit to support typing
from json import load, dump
from json.decoder import JSONDecodeError

from typing import TypedDict


def yesno(question: str) -> bool:
    """
    A simple yes or no question. Usage:
    ```python
    if yesno(question):
        ...
    else:
        ...
    ```
    """

    answer = input(question).casefold()
    return answer == "yes" or answer == "y"


class Data(TypedDict):
    languages: dict[str, str | None]
    words1: list[str]
    words2: list[str]


class JsonData(TypedDict):
    version: int | float
    info: dict[str, str | None]
    data: Data


class File:
    def __init__(self, filename: str | None = None):
        self.name = self.getFilename() if filename == None else filename
        self.data = self.loadFile()

    def getFilename(self) -> str:
        """Get user input to get the file"""

        # Prevent a blank input
        while True:
            self.filename = input("Filename: ")
            if self.filename == '':
                print('\033[2A')
            else:
                break

        # Add '.wrd' at the end if necessary
        if not self.filename.endswith('.wrd'):
            print(f"Filename: \033[1A{self.filename}.wrd\n         \033[1A")
            self.filename = self.filename + '.wrd'

        return self.filename

    def loadFile(self) -> JsonData:
        """
        Loads the `filename` file. If it is not specified or None,
        it asks the user for the filename using `file.getFilename()`
        """

        # Try to read the file, until goal
        while True:
            try:
                with open(self.filename, 'r') as json_file:
                    data: JsonData = load(json_file)
                break

            except FileNotFoundError as e:
                print(str(e)[10:])  # removing "[Errno 2] "
                if yesno("Would you like to create a new file? (Y/n) "):
                    self.createFile()
                else:
                    self.filename = self.getFilename()

            except JSONDecodeError as e:
                if yesno("File isn't in the right format. Would you like to overwrite the current file? (Y/n) "):
                    self.createFile()
                else:
                    exit()

        # Check the file
        if not self.checkFile():
            if yesno("The file is not complete. Would you like to overwrite it? (Y/n) "):
                self.createFile()
            else:
                exit()

        data["version"] = 0.1
        return data

    def createFile(self) -> JsonData:
        """Create a file with the basic file structure"""

        # Create file
        file = open(self.filename, 'w')
        file.close()

        # None becomes null in json files
        data: JsonData = {
            "version": 0.1,
            "info": {
                "title": None,
                "author": None
            },
            "data": {
                "languages": {
                    "lang1": None,
                    "lang2": None
                },
                "words1": [],
                "words2": []
            }
        }

        # User options
        print("Options: leave blank to leave empty")
        title = input("Title: ")
        author = input("Author: ")
        lang1 = input("First language (or term): ")
        lang2 = input("Second language (or definition): ")

        data["version"] = 0.1
        data["info"]["title"] = title if title != '' else None
        data["info"]["author"] = author if author != '' else None
        data["data"]["languages"]["lang1"] = lang1 if lang1 != '' else None
        data["data"]["languages"]["lang2"] = lang2 if lang2 != '' else None

        # Write the changes to the file
        with open(self.filename, 'w') as json_file:
            dump(data, json_file,
                 indent=4,
                 separators=(',', ': '))

        return data

    def checkFile(self, versionWarning: bool = True) -> bool:
        """Check the file for anything missing"""

        # Read the file
        with open(self.filename, 'r') as json_file:
            data: JsonData = load(json_file)

        # Warn the user when opening a file from a newer version
        if versionWarning:
            if data["version"] > 0.1:
                if yesno("This file is from an newer version. Would you like to continue? (Y/n) "):
                    # Change the version tag, so this doesn't happen again
                    data["version"] = 0.1
                    with open(self.filename, 'w') as json_file:
                        dump(data, json_file,
                             indent=4,
                             separators=(',', ': '))
                else:
                    exit()

        # Check if all keys exist
        try:
            data["version"]
            data["info"]["title"]
            data["info"]["author"]
            data["data"]["languages"]["lang1"]
            data["data"]["languages"]["lang2"]
        except KeyError:
            return False

        return True

    def containsWords(self) -> bool:
        return len(self.data["data"]["words1"]) >= 1 and len(self.data["data"]["words2"]) >= 1


class Words:
    def __init__(self, filename: str, data: JsonData) -> None:
        self.filename = filename
        self.data = data

    def editInfo(self) -> None:
        return

    def addWords(self) -> None:
        print("Type enter for the next word, or type an asterik for a " +
              "list of current words. To exit, leave an option blank.")

        words1: list[str] = []
        words2: list[str] = []

        word1 = ""
        break_outer = False
        i = 1
        while True:
            i = i + 1
            if i % 2 == 0:  # word 1
                while True:
                    word1 = input(f"{int(i/2)}: ")
                    if word1 == '':
                        break_outer = True
                    elif word1 == '*':
                        print(words1, words2)
                    else:
                        words1.append(word1)
                        break

            else:  # word 2
                while True:
                    word2 = input(
                        f"\033[1A{int(i/2-0.5)}: {word1} = ")
                    if not word2 == '':
                        words2.append(word2)
                        break
            if break_outer:
                break

    def editWords(self) -> None:
        return

    def learn(self) -> None:
        return

    def multiChoice(self) -> None:
        return

    def hints(self) -> None:
        return

    def test(self) -> None:
        return


def main():
    file = File()
    words = Words(file.filename, file.data)

    if file.containsWords():
        print("Action: Edit info (e), Edit words (w), Learn (l), Multiple choise (m) Hints (h), Test (t), Quit (q)")
        action = input("\n\033[1A> ").casefold()

        while True:
            match action:
                case 'e': words.editInfo()
                case 'w': words.editWords()
                case 'l': words.learn()
                case 'm': words.multiChoice()
                case 'h': words.hints()
                case 't': words.test()
                case 'q': return
                case _: action = input("\033[1A\033[2K> ")

    else:
        print("Action: Edit info (e), Add words (w), Quit (q)")
        action = input("\n\033[1A> ").casefold()

        while True:
            match action:
                case 'e': words.editInfo()
                case 'w': words.addWords()
                case 'q': return
                case _: action = input("\033[1A\033[2K> ")


if __name__ == '__main__':
    main()
