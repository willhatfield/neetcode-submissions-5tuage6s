class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gotHead = False

        slow, fast, groupPrev = head, head, dummy
        while fast:
            for i in range(1, k):
                fast = fast.next
                if fast is None:
                    return dummy.next
            
            temp = fast.next
            fast.next = None
            
            self.reverseToTail(slow)
            
            if not gotHead:
                dummy.next = fast
                gotHead = True
            
            groupPrev.next = fast
            slow.next = temp
            
            groupPrev = slow
            fast = slow.next
            slow = fast
        
        return dummy.next

        
    def reverseToTail(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev