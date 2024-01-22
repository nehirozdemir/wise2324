#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 09-2

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts.

"""

# Aufgabe 6


def power(exponent):
    """Refs

    https://stackoverflow.com/questions/5929107/decorators-with-parameters
    https://t.ly/5-gj9

    """

    def wrap(f):
        def wrapped_f(*args):
            sequence = args[0]
            index = 0
            for number in sequence:
                # We are editing the sequence
                if sequence[index] < 0:
                    print("No negative numbers allowed")
                    return None
                sequence[index] = number**exponent
                index += 1
            return f(sequence)

        return wrapped_f

    return wrap


@power(3)
def print_sum(sequence):
    """Print and return the sum of the sequence"""
    result = 0
    for number in sequence:
        result += number
    print("The sum of {} is {}".format(sequence, result))
    return result


@power(3)
def print_prod(sequence):
    """Print and return the product of the sequence"""
    result = 1
    for number in sequence:
        result *= number
    print("The product of {} is {}".format(sequence, result))
    return result


# Testaufrufe

if __name__ == "__main__":
    print_sum([1, 2, 3])
    print_prod([1, 2, 3])
    print_sum([1, -2, 3])
    print_prod([-1, 2, 3])
