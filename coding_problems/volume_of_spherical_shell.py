"""
The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753
"""

import math

def vol_shell(r1, r2):
    ret = (4 / 3) * (math.pi) * (r1**3 - r2**3)
    return abs(round(ret, 3))

print(vol_shell(3, 3))
print(vol_shell(7, 2))
print(vol_shell(3, 800))
