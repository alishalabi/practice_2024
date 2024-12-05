"""
Given a list of numbers, create a function that removes 25% from every number in the list except the smallest number, and adds the total amount removed to the smallest number.

Examples
show_the_love([4, 1, 4]) ➞ [3, 3, 3]

show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]

show_the_love([2, 100]) ➞ [27, 75]

From: https://edabit.com/challenge/pqpkRBP4YT5dwBDHm
"""

def show_the_love(arr):
    lowest_index = 0
    ret = arr
    for i in range(len(arr)):
        if arr[i] < arr[lowest_index]:
            lowest_index = i
    total_subracted = 0
    for i in range(len(arr)):
        if i != lowest_index:
            quarter = arr[i] / 4
            ret[i] -= quarter
            total_subracted += quarter
    ret[lowest_index] += total_subracted
    return ret

print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))
