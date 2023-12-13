"""
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])

Problem from: https://edabit.com/challenge/5XXXppAdfcGaootD9
"""

def sum_odd_and_even(arr):
    sum_evens = 0
    sum_odds = 0
    for number in arr:
        if number % 2 == 0:
            sum_evens += number
        else:
            sum_odds += number
    return [sum_evens, sum_odds]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
