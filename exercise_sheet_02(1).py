#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 02

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu den
einzelnen Aufgaben des Übungsblatts. Bitte verändern Sie jeweils nur
die Variablenzuweisungen, nicht aber die `print`-Befehle. Das würde
sonst unter Umständen Ihr Ergebnis verfälschen.

"""


# Aufgabe 1

A = "Python sagt \"Hallo!\""
print(A)

B = "Wie geht\'s?"
print(B)

C = "Python sagt \"Hallo, wie geht\'s?\""
print(C)


# Aufgabe 2

D = "Eine Zeile\nUnd noch eine Zeile"
print(D)

E = "Eigentlich erzeugt \\n einen Zeilenumbruch."
print(E)


# Aufgabe 3

QUOTE = "Python ist eine universelle, üblicherweise interpretierte höhere Programmiersprache."

F = 0
G = 11
H = 2
I = -17
J = 24
K = -1
print(QUOTE[F:G] + QUOTE[H] + QUOTE[I] + 2 * QUOTE[J] + QUOTE[K])

L = -73
M = 52
N = 5
print(QUOTE[:L] + "su" + QUOTE[48:M:2] + QUOTE[-6::N])


# Aufgabe 4

O = 1
P = 17835
print(O + 2 * P)

Q = 10
print((3 ** (Q - 1)) + 1) #** = power operator

R = 37
print(True and not R - 37)


# Zusatzaufgabe 5

# Antwort: In Python beginnt die Indexierung mit einem 0.
# es gilt H-0, A-1, L-2, L-3, O-4. Der 5. Buchstabe "existiert" nicht.


# Zusatzaufgabe 6

# Antwort: Tuple sind immutable, also unveraenderbar.
