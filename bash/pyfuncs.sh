#!/bin/bash


abs() {
    # Calculate the absolute value
    # of an integer. Usage:
    #   abs "$num"

    if [ "$1" -lt 0 ]; then
        echo "$((-$1))"
    else
        echo "$1"
    fi
}


all() {
    # Check if all elements in an array
    # evaluate to true. Usage:
    #   all "${array[@]}"

    for i in "$@"; do
        if [ "$i" != true ]; then
            echo false
            return
        fi
    done

    echo true
    return
}


any() {
    # Check if a single element in an
    # array evaluates to true. Usage:
    #   any "${array[@]}"

    for i in "$@"; do
        if [ "$i" == true ]; then
            echo true
            return
        fi
    done

    echo false
    return
}


bin() {
    # Returns the binary representation of
    # a number in the form '0b**'. Usage:
    #   bin $num

    result=""

    if [ "$1" -eq 0 ]; then
        echo "0b0"
        return
    elif [ "$1" -le 0 ]; then
        result=-
        set -- "$(abs "$1")"
    fi

    while [ "$1" -gt 0 ]; do
        result="$(($1 % 2))$result"
        set -- "$(($1 / 2))"
    done

    echo "0b$result"
    return
}
