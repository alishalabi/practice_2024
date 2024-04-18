"""
Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.


Return the number of dots that exist in the whole pentagon on the Nth iteration.

Examples
pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

pentagonal(3) ➞ 16

pentagonal(8) ➞ 141

From: https://edabit.com/challenge/st8mDxreMcuWxuz8c

Math formula for pentagonal number: (5n^2-5n+2)/2 (from: https://www.geeksforgeeks.org/centered-pentagonal-number/)
"""

def pentagonal(n):
    ret = (5 * n * n - 5 * n + 2) // 2
    return ret


print(pentagonal(1))
print(pentagonal(2))
print(pentagonal(3))
print(pentagonal(8))
