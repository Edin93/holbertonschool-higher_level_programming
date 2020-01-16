#!/usr/bin/python3
""" This module contains one function.
the following is a usage example of our matrix_divided function module, Ex:
>>> text_indentation("Hey you. \
... What's going on there?")
Hey you.
<BLANKLINE>
What's going on there?
<BLANKLINE>
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? or : character.
    """
    if text is None:
        raise TypeError("text must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    if len(text.strip()) == 0:
        raise TypeError("text must be a string")
    test = ".?:"
    ln = len(text)
    i = 0
    while i < ln:
        if text[i] == ' ' and text[i - 1] in test:
            i += 1
        if text[i] in test:
            print(text[i])
            print()
        else:
            print(text[i], end="")
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/5-text_indentation.txt')
