"""
Create a function that returns the number of characters shared between two words.

Examples
shared_letters("apple", "meaty") ➞ 2
# Since "ea" is shared between "apple" and "meaty".

shared_letters("fan", "forsook") ➞ 1

shared_letters("spout", "shout") ➞ 4
"""

def shared_letters(string1, string2):
    string1_dict = {}
    ret = 0
    for letter in string1:
        if letter not in string1_dict:
            string1_dict[letter] = 1
        else:
            string1_dict[letter] += 1
    for letter in string2:
        if letter in string1_dict and string1_dict[letter] > 0:
            ret += 1
            string1_dict[letter] -= 1
    return ret

print(shared_letters("apple", "meaty"))
print(shared_letters("fan", "forsook"))
print(shared_letters("spout", "shout"))
print(shared_letters("apple", "apples"))
