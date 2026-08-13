# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListRec(prev, curr):
            if not curr:
                return prev
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return reverseListRec(prev, curr)

        prev = None
        curr = head

        return reverseListRec(prev, curr)
        

