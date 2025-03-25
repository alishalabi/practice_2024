"""
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""

def invert(input):
    output = {}
    for key in input:
        output[input[key]] = key
    return output

print(invert({ "z": "q", "w": "f" }))
print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" }))
