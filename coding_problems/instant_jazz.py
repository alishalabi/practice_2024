"""
Create a function which concatenates the number 7 to the end of every chord in a list.
Ignore all chords which already end with 7.

Examples
jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

jazzify([]) ➞ []

Problem from: https://edabit.com/challenge/jhghtvT2s58FnDr5T
"""

def jazzify(chords):
    new_chords = []
    for chord in chords:
        if "7" in chord:
            new_chords.append(chord)
        else:
            new_chords.append(chord+"7")
    return new_chords

print(jazzify(["G", "F", "C"]))
print(jazzify(["Dm", "G", "E", "A"]))
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(jazzify([]))
