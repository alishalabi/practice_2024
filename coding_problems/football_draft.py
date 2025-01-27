"""
Create a system for N users to randomly get sorted into a draft order. Then, given a round R, return which user's turn it is
to draft.
"""

import random

def create_draft_order(arr):
    random.shuffle(arr)
    return arr

def current_drafter(arr, round):
    print(arr)
    index = (len(arr) - 1)  % round
    return arr[index]

arr1 = ["user1", "user2", "user3", "user4"]
# print(create_draft_order(arr1))

print(current_drafter(create_draft_order(arr1), 7))
