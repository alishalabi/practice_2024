"""
Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"

From: https://edabit.com/challenge/wcdS7MEL5gvr5SGsh
"""

def alphabet_index(alphabet, string):
    highest_index = 0
    ret = None
    alphabet_dictionary = {}
    counter = 1
    for letter in alphabet:
        alphabet_dictionary[letter] = counter
        counter += 1
    for letter in string:
        letter = letter.lower()
        if alphabet_dictionary[letter] > highest_index:
            highest_index = alphabet_dictionary[letter]
            ret = f"{highest_index}{letter}"
    return ret




alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(alphabet_index(alphabet, "Flavio"))
print(alphabet_index(alphabet, "Andrey"))
print(alphabet_index(alphabet, "Oscar"))
