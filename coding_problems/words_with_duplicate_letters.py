"""
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".

From: https://edabit.com/challenge/WS6hR6b9EZzuDTD26
"""

def no_duplicate_letters(sentence):
    word_array = sentence.split(" ")
    for word in word_array:
        all_letters = set()
        for letter in word:
            if letter in all_letters:
                return False
            else:
                all_letters.add(letter)
    return True

print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))
print(no_duplicate_letters("An apple a day keeps the doctor away."))
