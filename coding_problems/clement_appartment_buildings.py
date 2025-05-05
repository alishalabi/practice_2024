"""
https://www.youtube.com/watch?v=rw4s4M3hFfs&t=2051s&ab_channel=Cl%C3%A9mentMihailescu
"""

blocks = [
    {
    "gym": False,
    "school": True,
    "store": False
    },
    {
    "gym": True,
    "school": False,
    "store": False
    },
    {
    "gym": True,
    "school": True,
    "store": False
    },
    {
    "gym": False,
    "school": True,
    "store": False
    },
    {
    "gym": False,
    "school": True,
    "store": True
    },
]

def best_block(blocks):
    # lowest value
    lowest_value = None
    # current lowest index
    current_lowest_index = 0
    # iterate each block, calculate min distance for each req, assign value to total distance
    for index in range(len(blocks)):
        total_distance = 0
        for req in blocks[index]:
            left_pointer = index
            right_pointer = index
            if blocks[index][req] == True:
                pass
            else:
                left_pointer -=1
                right_pointer += 1
                


print(best_block(blocks))
