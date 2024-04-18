"""
Given the month and year as numbers, return whether that month contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False

From: https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
"""

# Info on datetime pulled from docs: https://docs.python.org/3/library/datetime.html

from datetime import date

def has_friday_13(month, year):
    d = date(year, month, 13)
    if d.weekday() == 4:
        return True
    else:
        return False

print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
