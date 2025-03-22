"""
Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator.
Return the sum of the fractions rounded to the nearest whole number.

Examples
sum_fractions([[18, 13], [4, 5]]) ➞ 2

sum_fractions([[36, 4], [22, 60]]) ➞ 9

sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) ➞ 11
"""

def sum_fractions(arr):
    # num1 = arr[0][0] / arr[0][1]
    # num2 = arr[1][1] / arr[1][1]
    # ret = round(num1 + num2)
    ret = 0
    for i in range(len(arr)):
        ret += arr[i][0] / arr[i][1]
    return round(ret)

print(sum_fractions([[18, 13], [4, 5]]) )
print(sum_fractions([[36, 4], [22, 60]]))
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
