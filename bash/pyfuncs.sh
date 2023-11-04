#!/bin/bash

abs() {
    # Calculate the absolute value
    # of an integer. Usage:
    #   abs "$num"

    if [ "$1" -lt 0 ]; then
        echo $((-$1))
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