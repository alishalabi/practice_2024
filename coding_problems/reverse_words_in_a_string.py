"""
Given an input string, reverse the string word by word.

Examples
reverse_words("the sky is blue") ➞ "blue is sky the"

reverse_words("  hello world!  ") ➞ "world! hello"

reverse_words("a good   example") ➞ "example good a"

From: https://edabit.com/challenge/SfEretprfmbbcTChT
"""

def reverse_words(sentence):
    sentence_arr = sentence.strip().split(" ")
    ret = ""
    for word in sentence_arr:
        if word == " ":
            sentence_arr.remove(word)
    for i in range(len(sentence_arr)):
        ret += sentence_arr[len(sentence_arr) - i - 1] + " "
    return ret

print(reverse_words("the sky is blue"))
print(reverse_words("  hello world!  "))
print(reverse_words("a good   example"))

# Note: still working on internal spaces
