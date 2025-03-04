"""
Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
"""

def stutter(word):
    first_two = str(word[0] + word[1])
    return f"{first_two}...{first_two}...{word}"

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))
