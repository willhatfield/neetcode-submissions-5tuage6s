# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast, slow = head, head
        slowPrev = None
        

        while fast and fast.next:
            slowPrev = slow
            fast = fast.next.next
            slow = slow.next
            
        if slowPrev:
            slowPrev.next = None
        
        
        head2 = self.reverse(slow)

        curr = head
        curr2 = head2
        while curr and curr2:
            next1 = curr.next
            next2 = curr2.next

            curr.next = curr2
            if next1:
                curr2.next = next1
            
            curr = next1
            curr2 = next2


    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev, curr = None, head

        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        
        return prev