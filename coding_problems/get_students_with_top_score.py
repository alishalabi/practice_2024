"""
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }

From: https://edabit.com/challenge/5KqHNS9wS97zN7Xyy
"""

def top_note(dictionary_of_objects):
    top_note = max(dictionary_of_objects["notes"])
    ret = {"name": dictionary_of_objects["name"], "top_note": top_note}
    return ret

print(top_note({ "name": "John", "notes": [3, 5, 4] }))
print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
print(top_note({ "name": "Zygmund", "notes": [1, 2, 3] }))
