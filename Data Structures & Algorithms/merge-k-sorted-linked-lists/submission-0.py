# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while True:
            minIdx, minVal = -1, float('inf')

            for i in range(len(lists)):
                if lists[i] and lists[i].val < minVal:
                    minIdx = i
                    minVal = lists[i].val
            
            if minIdx == -1:
                break
            curr.next = lists[minIdx]
            

            curr.next = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            curr = curr.next

        return dummy.next
