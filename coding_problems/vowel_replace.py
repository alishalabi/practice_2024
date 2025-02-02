"""
Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""

def replace_vowels(word, char):
    black_list = {"a", "e", "i", "o", "u", "y"}
    ret = ""
    for letter in word:
        if letter not in black_list:
            ret += letter
        else:
            ret += char
    return ret

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
