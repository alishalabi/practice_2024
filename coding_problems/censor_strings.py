"""
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

From: https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
"""

def uncensor(string, vowels):
    ret = ""
    remaining_vowels = vowels
    for character in string:
        if character != "*":
            ret += character
        else:
            ret += remaining_vowels[0]
            remaining_vowels = remaining_vowels[1:]
    return ret

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))
