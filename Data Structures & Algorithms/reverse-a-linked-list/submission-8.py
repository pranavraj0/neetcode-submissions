# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # can't iterate to end and recurse, don't have previous pointer
        # so the solution must start from head... 
        if not head:
            return None
        if not head.next:
            return head

        nextNode = head.next
        newHead = self.reverseList(head.next)
        nextNode.next = head
        head.next = None
        return newHead

        #how to bring head up from tail? 




        



        

        