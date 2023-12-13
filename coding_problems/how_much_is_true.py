"""
Create a function which returns the number of true values there are in an array.

Examples
countTrue([true, false, false, true, false]) ➞ 2

countTrue([false, false, false, false]) ➞ 0

countTrue([]) ➞ 0

Problem from: https://edabit.com/challenge/GLbuMfTtDWwDv2F73
"""

def countTrue(arr):
    count = 0
    for item in arr:
        if item == True:
            count += 1
    return count

print(countTrue([True, False, False, True, False]))
print(countTrue([False, False, False, False, False]))
print(countTrue([]))
