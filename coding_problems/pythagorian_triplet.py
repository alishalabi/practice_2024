"""
Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
"""

def is_triplet(num1, num2, num3):
    sorted_arr = sorted([num1, num2, num3])
    if (sorted_arr[0]**2 + sorted_arr[1]**2) == sorted_arr[2]**2:
        return True
    else:
        return False

print(is_triplet(3, 4, 5))
print(is_triplet(13, 5, 12))
print(is_triplet(1, 2, 3))
