"""
Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None


Notes
The frequency of the majority element must be strictly greater than 1/2.
If there is no majority element, return None.
If the list is empty, return None.

From: https://edabit.com/challenge/pQavNkBbdmvSMmx5x
"""

# Using maps
def majority_vote1(arr):
    my_map = {}
    majority_threshold = len(arr)/2
    for item in arr:
        if item not in my_map:
            my_map.update({item: 1})
        else:
            my_map[item] += 1
    for key in my_map.keys():
        if my_map[key] > majority_threshold:
            return key
    else:
        return None


# Using sorted list
def majority_vote2(arr):
    sorted_arr = sorted(arr)
    majority_threshold = len(arr)/2
    count = 0
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            count += 1
            if count > majority_threshold:
                return sorted_arr[i]
        else:
            count = 0
    return None



# print(majority_vote1(["A", "A", "B"]))
# print(majority_vote1(["A", "A", "A", "B", "C", "A"]))
# print(majority_vote1(["A", "B", "B", "A", "C", "C"]))

print(majority_vote2(["A", "A", "B"]))
# print(majority_vote2(["A", "A", "A", "B", "C", "A"]))
# print(majority_vote2(["A", "B", "B", "A", "C", "C"]))
