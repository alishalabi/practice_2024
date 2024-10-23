"""
Create a function that takes two number strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"

From: https://edabit.com/challenge/2RtztnzMDdyAj2MD3

"""

def add(number1, number2):
    if number1.isdigit() == False or number2.isdigit() == False:
        return "Invalid Operation"
    sum = int(number1) + int(number2)
    return str(sum)

print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
