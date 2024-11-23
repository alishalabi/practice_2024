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
    if len(pin) not in (4,6):
        return False
    if pin.isdigit() == False:
        return False
    return True

print(valid("1234"))
print(valid("45135"))
print(valid("89abc1"))
print(valid("900876"))
print(valid(" 4983"))
