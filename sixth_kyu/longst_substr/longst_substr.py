"""

Kata - Longest alphabetical substring

    Find the longest substring in alphabetical order.

    Eg: the longest alphabetical substring in asdfaaaabbbbcttavvfffffdf is aaaabbbbctt.

    There are tests with strings up to 10000 characters long so your code will need to be efficient.

    The input will only consist of lowercase characters and will be at least one letter long.
"""

__author__ = 'pejs and jejs'


def longest(s):
    """
    Takes a lowercase string and calculates the longest substring in alphabetical order
    :param s: a lowercase string at least one letter long
    :return: the longest substring of the input string in alphabetical order
    """

    # TODO - finish the solution. Initial idea is to compare every two characters. If next char is greater/equal to
    # TODO - previous char, accumulate the result in current_alpha_str. If not, compare if current_alpha_str is longer
    # TODO - than longest_alpha_str found so far. Return longest_alpha_str.

    previous_char = ''
    current_alpha_str = ''
    longest_alpha_str = ''
    for next_char in s:
        if next_char >= previous_char:
            pass
        else:
            pass
    return longest_alpha_str
