"""
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

Examples
shift_sentence("create a function") ➞ "freate c aunction"

shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

shift_sentence("edabit") ➞ "edabit"
"""

def shift_sentence(string):
    ret = ""
    parsed_array = string.split()
    if len(parsed_array) < 2:
        return string
    for index in range(len(parsed_array)):
        if index == 0:
            new_word = parsed_array[-1][0] + parsed_array[index][1:]
            ret += new_word
        else:
            new_word = parsed_array[index - 1][0] + parsed_array[index][1:]
            ret += " " + new_word
    return ret


print(shift_sentence("create a function"))
print(shift_sentence("it should shift the sentence"))
print(shift_sentence("the output is not very legible"))
print(shift_sentence("edabit"))
