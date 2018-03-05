#!/usr/bin/env python

"""
    Kata - Multiplies of 3 or 5

    Description:
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    Note: If the number is a multiple of both 3 and 5, only count it once.
"""

__author__ = 'pejs and jejs'


def solution(number):
    """
    Finds the sum of all multiples of 3 or 5 below given number.
    Example:
        10 returns 23 (3, 5, 6 and 9 are multiples of 3 or 5)
    :param number: an int number for which the sum is calculated
    :return: integer sum of all 3 or 5 multiplies below a number
    """
    #TODO - refactor the code using list comprehension (one liner)

    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
