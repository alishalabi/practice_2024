"""
Create a function that takes a list of numbers or strings and returns a list with the items from the
original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
"""

def advanced_sort(array):
    ret = []
    map = {}
    current_index = 0
    for item in array:
        if item not in map:
            map[item] = current_index
            current_index += 1
            ret.append([item])
        else:
            ret_index = map[item]
            ret[ret_index].append(item)

    return ret

print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))
