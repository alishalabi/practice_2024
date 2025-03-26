"""
Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.

Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6

is_equal([21, 35]) ➞ False

is_equal([0, 0]) ➞ True
"""

def is_equal(arr):
    sum1 = 0
    sum2 = 0
    for digit in str(arr[0]):
        sum1 += int(digit)
    for digit in str(arr[1]):
        sum2 += int(digit)
    if sum1 == sum2:
        return True
    else:
        return False

print(is_equal([105, 42]))
print(is_equal([21, 35]))
print(is_equal([0, 0]))
