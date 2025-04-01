"""
Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None
"""

def stupid_addition(num1, num2):
    if isinstance(num1, int) == True and isinstance(num2, int) == True:
        return str(num1) + str(num2)
    elif isinstance(num1, str) == True and isinstance(num2, str) == True:
        return int(num1) + int(num2)
    else:
        return None

print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))
