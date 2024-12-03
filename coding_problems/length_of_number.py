"""
Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1

Notes
The use of the len() function is prohibited.

From: https://edabit.com/challenge/2zKetgAJp4WRFXiDT
"""

def number_length(number):
    ret = 0
    for digit in str(number):
        ret += 1
    return ret

print(number_length(10))
print(number_length(5000))
print(number_length(0))
