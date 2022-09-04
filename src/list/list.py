#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import string
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


# =======================Exercise 6 ===================================
def proper_divisors(num: int) -> List[int]:
    divisors = []
    for n in range(1, num):
        if num % n == 0:
            divisors.append(n)
    return divisors


def read_user_input() -> str:
    word = input("Enter a word (blank line to quit): ")
    return word


def list_exercise6() -> None:
    """
    Exercise 6: List of Proper Divisors
    (36 Lines)
        A proper divisor of a positive integer, n, is a positive
        integer less than n which divides evenly into n. Write a
        function that computes all the proper divisors of a
        positive integer. The integer will be passed to the
        function as its only parameter. The function will return a list
        containing all the proper divisors as its only result. Complete
        this exercise by writing a main program that demonstrates the
        function by reading a value from the user and displaying the list
        of its proper divisors. Ensure that your main program only runs
         when your solution has not been imported into another file.
    """
    num = int(read_user_input())
    divisors = proper_divisors(num)
    print(divisors)


# =======================Exercise 7 ===================================
def perfect_number(number: int) -> bool:
    divisors = proper_divisors(number)
    total = 0
    for n in divisors:
        total += n
    if total == number:
        return True
    else:
        return False


def list_exercise7():
    """
    Exercise 7: Perfect Numbers
    (Solved, 35 Lines)
        An integer, n, is said to be perfect when the sum of all the
        proper divisors of n is equal to n. For example, 28 is a
        perfect number because its proper divisors are 1, 2, 4, 7 and
        14, and 1 + 2 + 4 + 7 + 14 = 28. Write a function that
        determines whether a positive integer is perfect. Your
        function will take one parameter. If that parameter is a
        perfect number than your function will return True. Otherwise,
        it will return False. In addition, write a main program that
        uses your function to identify and display all the perfect
        numbers between 1 and 10,000.
    """
    max_number = 10000
    perfect = []
    for n in range(1, max_number):
        if perfect_number(n):
            perfect.append(n)
    print(perfect)


# =======================Exercise 8 ===================================
def only_the_words(words: str) -> List[str]:
    result = []
    words = words.split()

    for word in words:

        while len(word) > 0 and word[-1] in string.punctuation:
            word = word[: len(word) - 1]
        while len(word) > 0 and word[1] in string.punctuation:
            word = word[2:]

        if len(word) > 0:
            if word[0] in string.punctuation:
                w = "".join([x for x in word if x not in string.punctuation])
            else:
                w = word
            if len(w) > 0:
                result += w.split()
    return result


def list_exercise8() -> None:
    """
    Exercise 8: Only theWords
    (38 Lines)
        In this exercise you will create a program that identifies all
        the words in a string entered by the user. Begin by writing a
        function that takes a string as its only parameter. Your
        function should return a list of the words in the string with
        the punctuation marks at the edges of the words removed. The
        punctuation arks that you must consider include commas,
        periods, question marks, hyphens, apostrophes, exclamation points,
        colons, and semicolons. Do not remove punctuation marks that
        appear in the middle of a word, such as the apostrophes used to
        form a contraction. For example, if your function is provided
        with the string "Contractions include: don’t, isn’t, and would
        not." then your function should return the list
        ["Contractions", "include", don’t", "isn’t", "and", "would not"].
    """
    word = read_user_input()
    words = only_the_words(word)
    print(words)


def main() -> None:
    # Passed.
    # list_exercise1()
    # Passed.
    # list_exercise2()
    # Passed.
    # list_exercise3()
    # Passed.
    # list_exercise4()
    # Passed.
    # list_exercise5()
    # Passed.
    # list_exercise6()
    # Passed.
    # list_exercise7()

    list_exercise8()


if __name__ == "__main__":
    main()
