#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our matrix_divided function module, Ex:
>>> text_indentation("Lorem ipsum dolor sit amet")
Lorem ipsum dolor sit amet
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? or : character.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    test = ".?:"
    ln = len(text)
    i = 0
    while text[i]:
        if text[i] in test:
            print()
            print()
        elif (text[i] == " " and text[i + 1] == '\\':
              print()
        else:
              print(text[i])
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/5-text_indentation.txt')
