"""
Write a function that calculates the factorial of a number recursively.

Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(1) ➞ 1

factorial(0) ➞ 1
"""

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))
