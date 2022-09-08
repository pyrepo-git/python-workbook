#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import string
import random
from typing import List

"""
Python data structures : list.
"""

MIN_NUMBER = 1
MAX_NUMBER = 49
MAX_NUMBERS = 6
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


# =======================Exercise 9 ===================================
def list_exercise9():
    """
    Exercise 9:Word byWord Palindromes
        Exercises 75 and 76 previously introduced the notion of
        a palindrome. Such palindromes examined the characters in a
        string, possibly ignoring spacing and punctuation marks,
        to see if the string was the same forwards and backwards.
        While palindromes are most commonly considered character by
        character, the notion of a palindrome can be extended to larger
        units. For example, while the sentence “Is it crazy how saying
        sentences backwards creates backwards sentences saying how
        crazy it is?” isn’t a character by character palindrome, it
        is a palindrome when examined a word at a time (and when
        capitalization and punctuation are ignored). Other examples of
        word by word palindromes include “Herb the sage eats sage, the
        herb” and “Information school graduate seeks graduate school
        information”. Create a program that reads a string from the
        user. Your program should report whether or not the entered
        string is a word by word palindrome. Ignore spacing and
        punctuation when determining the result.
    """
    word = read_user_input()
    word = word.lower()
    words = only_the_words(word)
    reverse_words = words[::-1]
    if words == reverse_words:
        print("Input string is palindrome")
    else:
        print("Input string is not palindrome")

    print(words)
    print(reverse_words)


# =======================Exercise 10 ===================================
def list_exercise10():
    """
    Exercise 10: Below and Above Average
        Write a program that reads numbers from the user until a blank
        line is entered. Your program should display the average of all
        of the values entered by the user. Then the program should
        display all of the below average values, followed by all of the
        average values (if any), followed by all of the above average
        values. An appropriate label should be displayed before each
        list of values.
    """
    numbers = []
    word = read_user_input()
    while word != "":
        num = int(word)
        numbers.append(num)
        word = read_user_input()

    total = 0
    for num in numbers:
        total += num
    if len(numbers) > 0:
        average = total / len(numbers)
        print(average)

        for val1 in numbers:
            if val1 < average:
                print(val1)
        print("-----")

        for val2 in numbers:
            if val2 == average:
                print(val2)
        print("-----")

        for val3 in numbers:
            if val3 > average:
                print(val3)


# =======================Exercise 11 ===================================
def concat_items(item1: str, item2: str) -> str:
    return "".join(item1) + " and " + "".join(item2)


def formatting_list(items: list) -> str:
    result = ""
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return concat_items(items[-2], items[-1])
    elif len(items) > 2:
        for index in range(len(items)):
            if index < len(items) - 2:
                result += "".join(items[index]) + ", "
            else:
                result += concat_items(items[-2], items[-1])
                return result
    else:
        return ""


def list_exercise11():
    """
    Exercise 11: Formatting a List
    When writing out a list of items in English, one normally separates
    the items with commas. In addition, theword “and” is normally
    included before the last item, unless the list only contains one
    item. Consider the following four lists:

    apples
    apples and oranges
    apples, oranges and bananas
    apples, oranges, bananas and lemons

    Write a function that takes a list of strings as its only
    parameter. Your function should return a string that contains
    all the items in the list, formatted in the manner described
    previously, as its only result. While the examples shown
    previously only include lists containing four elements or less,
    your function should behave correctly for lists of any length.
    Include a main program that reads several items from the user,
    formats them by calling your function, and then displays the result
    returned by the function.
    """
    word = read_user_input()
    items = word.split()
    text = formatting_list(items)
    print(word)
    print(items)
    print(text)


# =======================Exercise 12 ===================================
def list_exercise12():
    """
    Exercise 121: Random Lottery Numbers
        In order to win the top prize in a particular lottery, one must
        match all 6 numbers on his or her ticket to the 6 numbers
        between 1 and 49 that are drawn by the lottery
        organizer. Write a program that generates a random selection of
        6 numbers for a lottery ticket. Ensure that the 6 numbers
        selected do not contain any duplicates. Display the numbers in
        ascending order.
    """
    random_list = []
    for index in range(0, MAX_NUMBERS):
        ok = False
        n = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        while n in random_list:
            n = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        random_list.append(n)
    random_list.sort()
    print(random_list)


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
    # Passed.
    # list_exercise8()
    # Passed
    # list_exercise9()
    # Passed.
    # list_exercise10()
    # Passed.
    # list_exercise11()
    # Passed.
    list_exercise12()


if __name__ == "__main__":
    main()
