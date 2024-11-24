"""
Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True

valid("45135") ➞ False

valid("89abc1") ➞ False

valid("900876") ➞ True

valid(" 4983") ➞ False

From: https://edabit.com/challenge/xG2KB9T7mHgycGCSz
"""

def valid(pin):
    all_digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    if len(pin) not in (4,6):
        return False
    # if pin.isdigit() == False:
    #     return False
    for digit in pin:
        if digit not in all_digits:
            return False
    return True

print(valid("1234"))
print(valid("45135"))
print(valid("89abc1"))
print(valid("900876"))
print(valid(" 4983"))
