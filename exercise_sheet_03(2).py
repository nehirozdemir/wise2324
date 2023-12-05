#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 03

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts.

"""


CORPUS_TEXT = (
    "Good evening. Over 400000 million pounds were wiped off the "
    "value of shares this afternoon, when someone in the Stock "
    "Exchange coughed. Sport: capital punishment is to be "
    "re-introduced in the first and second division. Any player found "
    "tackling from behind or controlling the ball with the lower part "
    "of the arm will be hanged. But the electric chair remains the "
    "standard punishment for threatening the goalie. Finally, "
    "politics: the latest opinion poll published today shows Labour "
    "ahead with 40 %, the AA second with 38 % and not surprisingly "
    "Kentucky Fried Chicken running the Liberals a very close third. "
    "And now back to me. Hello. And now it's time to go over to Hugh "
    "Delaney in Paignton."
)


# Aufgabe 1

SENTENCES = CORPUS_TEXT.split(". ")
SENTENCES_COUNT = len(SENTENCES)
print(SENTENCES_COUNT)


# Aufgabe 2

CORPUS_CLEANED = CORPUS_TEXT.replace(".", "")\
.replace(",", "")\
.replace(":","")

VAR = CORPUS_CLEANED
print(isinstance(VAR, str))

TOKENS = CORPUS_CLEANED.split(" ")
TOKENS_COUNT = len(TOKENS)


TYPES = set(TOKENS)
TYPES_COUNT = len(TYPES)


# Aufgabe 3

KEYWORDS = ["Stock", "the", "40"]
FEATURES = {}


for KEYWORD in KEYWORDS:
    TEMP_LIST = []
    TEMP_LIST.append(len(KEYWORD))
    TEMP_LIST.append(KEYWORD.isnumeric())
    TEMP_LIST.append(KEYWORD.istitle())
    TEMP_LIST.append(CORPUS_TEXT.count(KEYWORD))
    FEATURES[KEYWORD]=TEMP_LIST
