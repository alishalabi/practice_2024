"""
Vowel Families
Write a function that selects all words that have all the same vowels (in any order and/or number) as the first word, including the first word.

Examples
same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]

same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]

same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
Notes
Words will contain only lowercase letters, and may contain whitespaces.
Frequency does not matter (e.g. if the first word is "loopy", then you can include words with any number of o's, so long as they only contain o's, and not any other vowels).
"""

def same_vowel_group(array):
    ret = []
    vowels = ["a", "e", "i", "o", "u", "y"]
    first_word = set()
    for letter in array[0]:
        if letter in vowels and letter not in first_word:
            first_word.add(letter)
    for word in array:
        word_vowels = set()
        for letter in word:
            if letter in vowels and letter not in word_vowels:
                word_vowels.add(letter)
        if word_vowels == first_word:
            ret.append(word)
    return ret

print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
