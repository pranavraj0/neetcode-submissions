# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                # add list1 to merged list
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                # add list2 to merged list
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        # will always be at least 1 left in non-empty list

        if not list1:
            curr.next = list2
        else:
            curr.next = list1
        
        return head.next

        