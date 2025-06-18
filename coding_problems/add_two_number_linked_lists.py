"""
The function input is two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list, in which the digits are also stored in reversed order. The class ListNode, building block of the linked list, is defined in the Tests tab.

Class definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
Examples
lt1 = ListNode(2)
lt1.add_data([4, 3])
lt2 = ListNode(5)
lt2.add_data([6, 4])
# print(lt1.get_data())    # [2, 4, 3]
# print(lt2.get_data())    # [5, 6, 4]
# print(342 + 465)         # 807

add_two_numbers(lt1, lt2).get_data() ➞ [7, 0, 8]
lt1 = ListNode(0)
lt2 = ListNode(0)
# print(lt1.get_data())    # [0]
# print(lt2.get_data())    # [0]
# print(0 + 0)             # 0

add_two_numbers(lt1, lt2).get_data() ➞ [0]
lt1 = ListNode(9)
lt1.add_data([9,9,9,9,9,9])
lt2 = ListNode(9)
lt2.add_data([9,9,9])
# print(lt1.get_data())    # [9, 9, 9, 9, 9, 9, 9]
# print(lt2.get_data())    # [9, 9, 9, 9]
# print(9999999 + 9999)    # 10009998

add_two_numbers(lt1, lt2).get_data() ➞ [8, 9, 9, 9, 0, 0, 0, 1]
Notes
The input linked lists can be of different lengths.
The returned reference has to point to the head of the new list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_data(array):
        for item in array:
            self.next = ListNode(val=item, next=None)

ll1 = ListNode(2)
ll1.add_data([4, 3])
print(ll1.val)
print(ll1.next.val)
