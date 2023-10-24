# tygoee/code-snippets

Just some small coding projects

These are some files that I made earlier on, or they were too small to make a repository. You are free to copy any of these contents without any mention, unless stated otherwise.

Some of these files moved to their own repository, and here you can see their early progress. Most old projects were uploaded with some differences in like formatting and type checking.

## Current projects

- bash/local_install.sh - Install apt packages locally, moved to [tygoee/papt](https://github.com/tygoee/papt)
- brainfck/helloworld.bf - Just hello world in brainfck, because I was curious
- cpp/tutorials/ - Tutorials I followed when starting with C++
- cpp/game/ - I was trying trying to make a game with some friends, later deleted it ([tygoee/ww3game](#))
- python/getimages/ - My first 'big' project: getting images from a online book viewer and making a pdf
- python/wrds/ - An unfinished terminal project for practicing words, inspired by [https://wrts.nl](https://studygo.com/nl/)
- python/autolibs/ - A way to import libraries automatically (this is good practise)
- javascript/befron/ - I helped someone with a discord bot, those were my files

## Running code

Most projects are run pretty intuitively, but here are some instructions:

First, of course, clone the git repo:

    git clone https://github.com/tygoee/code

### Bash

If you have linux (or macos?) installed, cd into the directory, give the file execute permissions and run the file:

    cd bash/(directory)
    chmod +x file.sh
    ./file.sh

If you have windows, install WSL and do the same.

### Brainfck

Install a [Brainfck interpreter](https://github.com/pocmo/Python-Brainfuck) and run the file:

    git clone https://github.com/pocmo/Python-Brainfuck
    cd Python-Brainfuck
    mkdir -p ~/.local/bin/
    cp -t ~/.local/bin/ brainfuck.py getch.py

    cd brainfck/(directory)
    brainfuck file.bf

### C++

Install [gcc/g++](https://gcc.gnu.org/) and run the file with `g++ file.cpp`. Files here don't contain any imports or libraries, so you don't need any flags to include libraries or other files. Note that some files I made are Windows-only, because they use standard headers like `conio.h`.

### JavaScript

When you have [node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed, cd into the directory, install the required modules and run the main file:

    cd javascript/(directory)
    npm install
    node file.js

### Python

Assuming you have [Python](https://www.python.org/) installed, cd into the folder, make a virtual environment and install `requirements.txt`:

    cd python/(directory)
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt

Then, just run the main python file with `python3 file.py`

---

© Tygo Everts | 2022 - 2023  
This code is licensed under the Unlicense,  
you can do anything you want with it.
