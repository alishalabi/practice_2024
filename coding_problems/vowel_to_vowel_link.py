"""
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False


Notes
You can expect sentences in only lowercase, with no punctuation
"""

def vowel_links(text):
    vowels = ["a", "e", "i", "o", "u"]
    split_list = text.split(" ")
    for i in range(len(split_list) - 1):
        if split_list[i][-1] in vowels and split_list[i+1][0] in vowels:
            return True
    return False

print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))
