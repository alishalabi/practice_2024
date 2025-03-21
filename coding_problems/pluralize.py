"""
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
Notes
This is an oversimplification of the English language so no edge cases will appear.
Only focus on whether or not to add an s to the ends of words.
All tests will be valid.

From: https://edabit.com/challenge/LR98GCwLGYPSv8Afb
"""

def pluralize(arr):
    histogram = {}
    ret = set()
    for word in arr:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    for key in histogram.keys():
        if histogram[key] == 1:
            ret.add(key)
        else:
            pluralized = str(key + "s")
            ret.add(pluralized)
    return ret

print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))
