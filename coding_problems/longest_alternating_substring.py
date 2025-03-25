"""
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.
"""

def is_even(digit):
    if int(digit) % 2 == 0:
        return True
    else:
        return False

def is_valid_even_odd(item1, item2):
    if is_even(item1) == True and is_even(item2) == False:
        return True
    elif is_even(item1) == False and is_even(item2) == True:
        return True
    else:
        return False


def longest_substring(input):
    ret = input[0]
    for i in range(len(input) - 1):
        current_substring = input[i]
        if is_valid_even_odd(input[i], input[i+1]) == True:
            current_substring += input[i+1]
            if len(current_substring) > len(ret):
                ret = current_substring
        else:
            pass
    return ret

print(longest_substring("225424272163254474441338664823"))
