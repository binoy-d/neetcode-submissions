# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        v
        0 -> 1 -> 2 -> 3
        curr = 0
        out = 0
        curr.next = 1
        
        out = curr.next

        """
        curr, prev = head, None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev