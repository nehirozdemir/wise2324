#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 06

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts.

"""
import copy
import random

# Aufgabe 1

def add_snake(snake, skill, template):
    """Adds a snake to a given list."""
    # newList = [("Cobra", "Venom"), ("Boa", "Constriction")]
    new_list = template.copy()
    # add a new tuple at the end of the list without changing the input list
    new_list.append(tuple((snake, skill)))
    return new_list


# Aufgabe 2

def is_perfect_number(number):
    """Determines whether a given number is perfect."""
    sum_of_divisors = 0
    range_upper_limit = int(number/2) + 1

    for i in range(1, range_upper_limit):
        if number % i == 0:  # % operator is modulus in python
            sum_of_divisors += i  # sumOfDivisors = sumOfDivisors + i

    if sum_of_divisors == number:
        return True

    return False


# Aufgabe 3

def append_square(number, numbers=None):
    """shows if a number is perfect"""
    if numbers is None:
        numbers = []
    squared_number = number ** 2
    numbers.append(squared_number)
    return numbers


# Aufgabe 4

def factorial(number):
    """Calculates the faculty of a given number."""
    # RecursionError: maximum recursion depth exceeded in comparison
    # Definitionsweise muss die Faktorialsgrenze 1 sein. Es gibt
    # eine Rekursionsgrenze in Python. Ohne Grenze wird die Rekursion
    # für immer andauern und es wird zum Error führen.
    if number == 1:
        return number

    return number * factorial(number - 1)


# Aufgabe 5

def euros_to_dollars(customers):
    """Converts Euros to Dollars."""
    # Ref: https://thispointer.com/python-how-to-copy-a-dictionary-shallow-copy-vs-deep-copy/
    # customers.copy() does not copy the items other than primitive data types such list data type
    # in our example Euro values are list data type
    # so it is necessary to deepcopy the dictionary
    new_customers = copy.deepcopy(customers)
    for name in new_customers:
        for index, euro in enumerate(new_customers[name]):
            new_customers[name][index] = euro * 1.5
    return new_customers



# Aufgabe 6

def print_random_chess_position():
    """Prints a random chess position."""
    # Strings haben keine Choice-Attribute. Bei der Berechnung von “random” der Vertikalen,
    # wurde die erste random Variable, die ein String ist,
    # (ein zugewaehlter Buchstabe aus der horizontalen Liste), berücksichtigt.
    horizontal = list("ABCDEFGH")
    vertical = list("12345678")
    random_str = random.choice(horizontal)  # str
    print("Horizontal: {}".format(random_str))
    random_str = random.choice(vertical)
    print("Vertikal: {}".format(random_str))


# Testaufrufe

if __name__ == "__main__":

    SNAKES = [("Cobra", "Venom"), ("Boa", "Constriction")]
    MY_SNAKES = add_snake("Rattlesnake", "Venom", SNAKES)
    print(MY_SNAKES)
    print(SNAKES)  # Unverändert

    print("27 ist eine perfekte Zahl:", is_perfect_number(27))
    print("28 ist eine perfekte Zahl:", is_perfect_number(28))

    print(append_square(7, numbers=[9, 4]))
    print(append_square(1, numbers=[]))
    print(append_square(2))
    print(append_square(3))
    NUMBERS = []
    print(append_square(4, NUMBERS))
    print(append_square(5, NUMBERS))

    #print("Fakultät von 3 ist:", factorial(3))
    #print("Fakultät von 5 ist:", factorial(5))

    CUSTOMER_EUROS = {"Charles": [27, 12], "Jacques": [31, 38]}
    CUSTOMER_DOLLARS = euros_to_dollars(CUSTOMER_EUROS)
    print("Rechnung in Währung Euro:")
    print(CUSTOMER_EUROS)
    print("Rechnung in Währung Dollar:")
    print(CUSTOMER_DOLLARS)

    #print_random_chess_position()
