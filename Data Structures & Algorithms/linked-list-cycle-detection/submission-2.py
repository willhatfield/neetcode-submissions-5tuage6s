# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
            
        fast = head.next
        slow = head

        if fast is None:
            return False

        while fast.next is not None and slow is not None:
            if slow is fast:
                return True
            
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                return False
        
        return False


