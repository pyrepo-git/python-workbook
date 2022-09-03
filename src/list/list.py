#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from typing import List

"""
Python data structures : list.
"""

values: List[int] = []


# =======================Exercise 1 ===================================
def list_exercise1() -> None:
    """
    Exercise 1: Sorted Order
    (Solved, 22 Lines)
        Write a program that reads integers from the user and stores
        them in a list. Your program should continue reading values
        until the user enters 0. Then it should display all the values
        entered by the user (except for the 0) in ascending order, with
        one value appearing on each line. Use either the sort method or
        the sorted function to sort the list.
    """

    # Read values from the user and store them in a list until a 0 is entered
    num = int(input("Enter a number (0 to quit): "))
    while num != 0:
        values.append(num)
        num = int(input("Enter a number (0 to quit): "))

    # Sort values into ascending order
    values.sort()

    # Display the values in ascending order
    print("The values, sorted into ascending order, are:")
    for num in values:
        print(num)


# =======================Exercise 2 ===================================
def list_exercise2() -> None:
    """
    Exercise 2: Reverse Order
    (20 Lines)
        Write a program that reads integers from the user and stores
        them in a list. Use 0 as a sentinel value to mark the end of
        the input. Once all the values have been read your program
        should display them (except for the 0) in reverse order, with
         one value appearing on each line.
    """
    # Read values from the user and store them in a list until a 0 is entered
    num = int(input("Enter a number (0 to quit): "))
    while num != 0:
        values.append(num)
        num = int(input("Enter a number (0 to quit): "))

    # Revers values (method 1)
    values1 = values[::-1]
    # Display the values in revers order
    print("The values, sorted into ascending order, are:")
    for num in values1:
        print(num)

    # Revers values (method 2)
    values.reverse()

    # Display the values in revers order
    print("The values, sorted into ascending order, are:")
    for num in values:
        print(num)


# =======================Exercise 3 ===================================
def remove_outliers(data: list, num_outliers: int) -> list:
    """
    Remove the outliers from a list of values
        @param data the list of values to process
        @param num_outliers outliers the number of smallest and largest
         values to remove
        @return a new copy of data where the values are sorted into
         ascending order and the smallest and largest values have been
          removed
    """
    # Create a new copy of the list that is in sorted order
    retval = sorted(data)

    # Remove num_outliers largest and
    # smallest values
    for n in range(num_outliers):
        retval.pop()
        retval.pop(0)

    return retval


def list_exercise3() -> None:
    """
    Exercise 3: Remove Outliers
    (Solved, 44 Lines)
        When analysing data collected as part of a science experiment
        it may be desirable to remove the most extreme values before
        performing other calculations. Write a function that takes a
        list of values and non-negative integer, n, as its
        parameters. The function should create a new copy of the list
        with the n the largest elements and the n the smallest elements
        removed. Then it should return the new copy of the list as the
        function’s only result. The order of the elements in the
        returned list does not have to match the order of the elements
        in the original list. Write a main program that demonstrates
        your function. It should read a list of numbers from the user
        and remove the two largest and two smallest values from it by
        calling the function described previously. Display the list
        with the outliers removed, followed by the original list. Your
        program should generate an appropriate error message if the
         user enters less than 4 values.
    """
    numbers = []
    # Read values from the user and store them in a list until a 0 is entered
    s = input("Enter a value (blank line to quit): ")
    while s != "":
        num = float(s)
        numbers.append(num)
        s = input("Enter a value (blank line to quit): ")

    if len(numbers) < 4:
        print("You did’t enter enough values.")
    else:
        print("With the outliers removed: ", remove_outliers(numbers, 2))
        print("The original data: ", numbers)


# =======================Exercise 4 ===================================
def list_exercise4() -> None:
    """
    Exercise 4:Avoiding Duplicates
    (Solved, 21 Lines)
        In this exercise, you will create a program that reads words
        from the user until the user enters a blank line. After the user
        enters a blank line your program should display each word
        entered by the user exactly once. The words should be displayed
        in the same order that they were first entered.
    """
    words = []
    word = input("Enter a word (blank line to quit): ")
    while word != "":
        # Add word to the list if
        # it is not already present in it
        if word not in words:
            words.append(word)
        word = input("Enter a word (blank line to quit): ")

    for word in words:
        print(word)


# =======================Exercise 5 ===================================
def list_exercise5() -> None:
    """
    Exercise 5: Negatives,Zeros and Positives
    (Solved, 36 Lines)
        Create a program that reads integers from the user until a
        blank line is entered. Once all the integers have been read
        your program should display all the negative numbers, followed
        by all the zeros, followed by all the positive numbers.Within
        each group the numbers should be displayed in the same order
        that they were entered by the user. For example, if the user
        enters the values 3, -4, 1, 0, -1, 0, and -2 then your program
        should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
        should display each value on its own line.
    """
    positives = []
    zeros = []
    negatives = []

    line = input("Enter integer (blank - to quit): ")
    while line != "":
        num = int(line)
        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeros.append(num)
        line = input("Enter integer (blank - to quit): ")

    for n in negatives:
        print(n)

    for n in zeros:
        print(n)

    for n in positives:
        print(n)


def main() -> None:
    # Passed.
    # list_exercise1()
    # Passed
    # list_exercise2()
    # Passed
    # list_exercise3()
    # Passed
    # list_exercise4()

    list_exercise5()


if __name__ == "__main__":
    main()
