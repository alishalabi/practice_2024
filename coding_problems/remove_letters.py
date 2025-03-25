"""
Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
"""

def remove_letters(arr, word):
    ret = []
    my_word = word
    # removed = []

    for letter in arr:
        if letter in my_word:
            my_word.replace(letter, "", 1)
        else:
            ret.append(letter)
    return ret

# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
