"""
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])
Notes
Count 0 as an even number.

From: https://edabit.com/challenge/5XXXppAdfcGaootD9
"""

def sum_odd_and_even(arr):
    sum_odd = 0
    sum_even = 0
    for number in arr:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return [sum_even, sum_odd]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
