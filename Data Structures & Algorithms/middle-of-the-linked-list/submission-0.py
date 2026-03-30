# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = ListNode(0, head)
        fast, slow = fast.next, slow.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow