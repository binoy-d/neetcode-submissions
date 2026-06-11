# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
               s           f
        [0, 1, 2, 3, 4, 5, 6]
        approach:
        - split list into halves with slow/fast pointer
        - merge the halves
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # slow ends up at halfway point, fast ends up as none


        l1 = head
        second_half = slow.next
        # since slow is at midpoint, we want to call that the end of the first list
        # which will become the end of the final list
        prev = slow.next = None

        # reverse second half
        while second_half:
            nextNode = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = nextNode
        
        # at this point, head is just the first half
        # prev is reversed lists head, now merge them
        first, second = head, prev
        
        while second:
            # store next 
            next1, next2 = first.next, second.next
            # insert second in betweenm
            first.next = second
            second.next = next1
            # shift
            first = next1
            second = next2

