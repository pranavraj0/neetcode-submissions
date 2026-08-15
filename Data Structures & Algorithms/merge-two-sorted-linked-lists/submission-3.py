# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            print(head, curr)
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    curr = list1
                    list1 = list1.next
                else:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next

                # add list1 curr to list
            else:
                if not head:
                    head = list2
                    curr = list2
                    list2 = list2.next
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return head
                    

                # add list2 curr to list

        