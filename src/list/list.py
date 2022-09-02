#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from typing import List

"""
Python data structures : list.
"""
values: List[int] = []


def lest_exercise1() -> None:
    """
    (Solved, 22 Lines)
        Write a program that reads integers from the user and stores them in
        a list. Your program should continue reading values until the user
        enters 0. Then it should display all of the values entered by the user
        (except for the 0) in ascending order, with one value appearing on
        each line. Use either the sort method or the sorted function.
        to sort the list.
    """

    # Read values from the user and store them in a list until a 0 is entered
    line = input("Enter a number (0) line to quit: ")
    while line != "0":
        num = int(line)
        values.append(num)

        line = input("Enter a number (0) line to quit: ")

    # Sort values into ascending order
    values.sort()

    # Display values
    for v in values:
        print(v)


def main() -> None:
    lest_exercise1()


if __name__ == "__main__":
    main()
