"""
The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
"""

def reverse(word):
    ret = ""
    for char in reversed(word):
        if char.islower():
            ret += char.upper()
        else:
            ret += char.lower()
    return ret


print(reverse("Hello World"))
print(reverse("ReVeRsE"))
print(reverse("Radar"))
