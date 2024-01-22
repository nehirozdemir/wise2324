#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 09

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts.

"""


KNIGHTS = [("Arthur", 34), ("Bedevere", 33), ("Galahad", 32), ("Lancelot", 36)]


# Aufgabe 1


def sort_by_age(knights):
    """
    Sort knights by age in ascending order
    Ref: https://stackoverflow.com/questions/10695139/sort-a-list-
    of-tuples-by-2nd-item-integer-value
    """
    return sorted(knights, key=lambda x: x[1])


# Aufgabe 2


def young_knights(knights):
    """
    Filter knights younger than 34
    Ref: https://ipcisco.com/lesson/python-lambda-function/
    """
    return list(filter(lambda x: (x[1] < 34), knights))


# Aufgabe 3


def get_knight_names(knights):
    """
    Returns only the knight name
    Ref: https://www.tutorialspoint.com/how-to-get-the-first-element-in-list-of-tuples-in-python
    """
    return [knight[0] for knight in knights]


# Aufgabe 4


def convert_to_dict(knights):
    """
    Gives list's tuples in the form of dict elements
    Ref:https://www.tutorialspoint.com/python-program-to-convert-dictionary-values-to-strings
    """
    return {key: str(value) for key, value in dict(knights).items()}


# Aufgabe 5


def prime_numbers():
    """
    A prime number is a whole number greater than 1
    whose only factors are 1 and itself.
    """
    num = 2
    while True:
        prime = 0
        # i is always x minus 1
        # thus, we never divide x to itself
        for i in range(2, num):
            if num > 1 and num % i == 0:
                prime += 1
        if prime == 0:
            yield num
        num += 1


# Testaufrufe

if __name__ == "__main__":
    print(sort_by_age(KNIGHTS))
    print(young_knights(KNIGHTS))
    print(get_knight_names(KNIGHTS))
    print(convert_to_dict(KNIGHTS))
    NUMBERS = prime_numbers()
    print([next(NUMBERS) for _ in range(20) if NUMBERS is not None])
