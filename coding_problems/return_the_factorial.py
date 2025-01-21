"""
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

Examples
factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800
"""

def factorial(number):
    ret = 1
    current_number = number
    while current_number > 1:
        ret = ret * current_number
        current_number -= 1
    return ret

print(factorial(3))
print(factorial(5))
print(factorial(13))
