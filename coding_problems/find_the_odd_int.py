"""
Create a function that takes a list and finds the integer which appears an odd number of times.

Examples
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
"""

def find_odd(arr):
    dict = {}
    for int in arr:
        if int not in dict:
            dict[int] = 1
        else:
            dict[int] += 1
    for item in dict:
        if dict[item] % 2 == 1:
            return item


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))
