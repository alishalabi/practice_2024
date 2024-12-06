"""
Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

Vowel	Number
A	4
E	3
I	1
O	0
U	0
Examples
sum_of_vowels("Let\'s test this function.") ➞ 8

sum_of_vowels("Do I get the correct output?") ➞ 10

sum_of_vowels("I love edabit!") ➞ 12

"""

def sum_of_vowels(sentence):
    vowel_values = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    sum = 0
    for letter in sentence:
        if letter.lower() in vowel_values:
            sum += vowel_values[letter.lower()]
    return sum

print(sum_of_vowels("Let\'s test this function."))
print(sum_of_vowels("Do I get the correct output?"))
print(sum_of_vowels("I love edabit!"))
