"""
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True

From: https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
"""

def is_disarium(number):
    disarium_sum = 0
    position = 1
    for digit in str(number):
        factor = int(digit) ** position
        disarium_sum += factor
        position += 1
    if disarium_sum == number:
        return True
    else:
        return False

print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(466))
print(is_disarium(8))
