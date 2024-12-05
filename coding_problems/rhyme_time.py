"""
Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.

Examples
does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True

does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.

does_rhyme("You are off to the races", "a splendid day.") ➞ False

does_rhyme("and frequently do?", "you gotta move.") ➞ False

Note: https://edabit.com/challenge/jwiJNMiCW6P5d2XXA
"""

def does_rhyme(sen1, sen2):
    all_vowels = ["a", "e", "i", "o", "u", "y"]
    last_word1 = sen1.split(" ")[-1]
    last_word2 = sen2.split(" ")[-1]
    vowels1 = []
    vowels2 = []
    for letter in last_word1:
        if letter.lower() in all_vowels:
            vowels1.append(letter.lower())
    for letter in last_word2:
        if letter.lower() in all_vowels:
            vowels2.append(letter.lower())
    if vowels1 == vowels2:
        return True
    else:
        return False


print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))
