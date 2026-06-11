# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """

        head = None
        curr_1 = list1
        curr_2 = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        tail = head
        while (curr_1 is not None) or (curr_2 is not None):
            

            next_to_add = None
            
            # get min node between curr_1 and curr_2
            # push to next the min
            
            if curr_1 is None:
                next_to_add = curr_2
                curr_2 = curr_2.next
            elif curr_2 is None:
                next_to_add = curr_1
                curr_1 = curr_1.next 
            elif curr_1.val < curr_2.val:
                next_to_add = curr_1
                curr_1 = curr_1.next
            else:
                next_to_add = curr_2
                curr_2 = curr_2.next

            # initial
            if head is None:
                head = next_to_add
                tail = head
            else:
                # set tail's next to the one to add
                tail.next = next_to_add
                # move tail
                tail = tail.next 

        return head 
