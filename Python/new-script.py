#!/bin/python3

import sys # system functions and parameters
from datetime import datetime as dt # import with alias

print(dt.now())

my_name = "Andrew"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                     hello                     "
print(too_much_space.strip())

print("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

# Dictionaries - key/value pairs {}
drinks = {
    "White Russian": 7, 
    "Old Fashioned": 10, 
    "Lemon Drop": 8
}

print(drinks)

employees = {
    "Finance": [
        "Bob",
        "Linda",
        "Tina"
    ],
    "IT": [
        "Gene",
        "Louise",
        "Teddy"
    ],
    "HR": [
        "Rick",
        "Morty"
    ]
}

print(employees)

employees["Legal"] = "Mr. Frond"
print(employees)

employees.update(
    {
        "Sales": [
            "Andy",
            "Ollie"
        ]
    }
)
print(employees)

drinks["White Russian"] = 8
print(drinks.get("White Russian"))