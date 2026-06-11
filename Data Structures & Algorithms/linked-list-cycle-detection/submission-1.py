# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        slow = head
        fast = slow.next

        # move fast 2, move slow 1

        while slow is not None and fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next

            # if the end is reachable, there's no cycle
            if not fast:
                return False
            else:
                fast = fast.next
        return False

                