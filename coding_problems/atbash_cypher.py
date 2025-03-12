"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
"""

def atbash(string):
    ret = ""
    lower_key = "abcdefghijklmnopqrstuvwxyz"
    upper_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in string:
        if letter in lower_key:
            new_index = 25 - lower_key.index(letter)
            ret += lower_key[new_index]
        elif letter in upper_key:
            new_index = 25 - upper_key.index(letter)
            ret += upper_key[new_index]
        else:
            ret += letter
    return ret

print(atbash("apple"))
print(atbash("zkkov"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))
