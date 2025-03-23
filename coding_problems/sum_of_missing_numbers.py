"""
Create a function that returns the sum of missing numbers from the given list.

Examples
sum_missing_numbers([4, 3, 8, 1, 2]) ➞ 18
# 5 + 6 + 7 = 18

sum_missing_numbers([17, 16, 15, 10, 11, 12]) ➞ 27
# 13 + 14 = 27

sum_missing_numbers([1, 2, 3, 4, 5]) ➞ 0
# No Missing Numbers (i.e. all numbers in [1, 5] are present in the list)
"""

def sum_missing_numbers(arr):
    ret = 0
    for number in range(min(arr), max(arr)):
        if number not in arr:
            ret += number
    return ret

print(sum_missing_numbers([4, 3, 8, 1, 2]))
print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
print(sum_missing_numbers([1, 2, 3, 4, 5]))
