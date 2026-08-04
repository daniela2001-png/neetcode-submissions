# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
i = -1 
while abs(i) <= len(lista):
    print(lista[i])
    i = i - 1
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # where we are now
        current = head
        # the node I'm leaving
        prev = None
        # the one that stores my old next pointer
        next_node = None
        while current != None:
            next_node = current.next
            # save old pointer before visiting my next pointer
            current.next = prev
            prev = current
            # this is gonna make that current in the last iter leave as None
            current = next_node
        return prev
        