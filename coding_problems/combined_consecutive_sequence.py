"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True

Notes
The input lists will have unique values.
The input lists can be in any order.

From: https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
"""

def consecutive_combo(arr1, arr2):
    combined_list = sorted(arr1 + arr2)
    for i in range(len(combined_list) - 1):
        if combined_list[i+1] != (combined_list[i] + 1):
            return False
    return True


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(consecutive_combo([44, 46], [45]))
