"""
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
"""

def rearranged_difference(number):
    number_dict = {}
    pre_sorted_keys = []
    for digit in str(number):
        if digit not in pre_sorted_keys:
            pre_sorted_keys.append(digit)
        if digit not in number_dict:
            number_dict[digit] = 1
        else:
            number_dict[digit] += 1
    sorted_keys = sorted(pre_sorted_keys)
    lowest_number = ""
    highest_number = ""
    for key in sorted_keys:
        lowest_number += (key * number_dict[key])
        highest_number = (key * number_dict[key]) + highest_number
    ret = int(highest_number) - int(lowest_number)
    return ret



print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
