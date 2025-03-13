"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters.
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). I

Examples
caesarCipher("middle-Outz", 2) ➞ "okffng-Qwvb"

// m -> o
// i -> k
// d -> f
// d -> f
// l -> n
// e -> g
// -    -
// O -> Q
// u -> w
// t -> v
// z -> b

caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5)
➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

caesarCipher("A friend in need is a friend indeed", 20)
➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
"""

def caesarCipher(string, shift):
    ret = ""
    lower_key = "abcdefghijklmnopqrstuvwxyz"
    upper_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in string:
        if letter in lower_key:
            old_index = lower_key.index(letter)
            new_index = (old_index + shift) % 26
            ret += lower_key[new_index]
        elif letter in upper_key:
            old_index = upper_key.index(letter)
            new_index = (old_index + shift) % 26
            ret += upper_key[new_index]
        else:
            ret += letter
    return ret

print(caesarCipher("middle-Outz", 2))
print(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5))
print(caesarCipher("A friend in need is a friend indeed", 20))
