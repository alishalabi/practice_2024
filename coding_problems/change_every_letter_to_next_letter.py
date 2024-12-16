"""
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
Examples
move("hello") ➞ "ifmmp"

move("bye") ➞ "czf"

move("welcome") ➞ "xfmdpnf"
"""

def move(word):
    letter_arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                    "w", "x", "y", "z"]
    ret = ""
    for letter in word:
        next_index = letter_arr.index(letter) + 1
        ret += letter_arr[next_index]
    return ret

print(move("hello"))
print(move("bye"))
print(move("welcome"))
