"""
Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

Examples
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"
"""

def name_shuffle(name):
    arr = name.split()
    return f"{arr[1]} {arr[0]}"

print(name_shuffle("Donald Trump"))
print(name_shuffle("Rosie O'Donnell"))
print(name_shuffle("Seymour Butts"))
