"""
Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

Examples
line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41

Problem from: https://edabit.com/challenge/3Ekam9jvbNKHDtx4K
"""

def line_length(point1, point2):
    side1 = point1[0] - point2[0]
    side2 = point1[1] - point2[1]
    side3 = ((side1 ** 2) + (side2 ** 2))**(1/2)
    return side3

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))
