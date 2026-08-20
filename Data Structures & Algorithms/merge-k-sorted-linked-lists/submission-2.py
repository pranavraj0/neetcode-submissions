# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeSortKListsRec(lists, l, r):
            
            if r - l + 1 <=1:
                return
            
            m = (l + r) // 2
            mergeSortKListsRec(lists, l, m) #list[l] sorts 
            mergeSortKListsRec(lists, m + 1, r)

            merge(lists, l, m, r)
            return
        
        # 
        def merge(lists, l, m, r):
            tempL = lists[l]
            tempM = lists[m + 1]

            head = ListNode(0)
            curr = head
            while tempL and tempM:
                if tempL.val <= tempM.val:
                    curr.next = tempL
                    tempL = tempL.next
                else:
                    curr.next = tempM
                    tempM = tempM.next
                curr = curr.next
            
            if tempL:
                curr.next = tempL
            if tempM: 
                curr.next = tempM
            
            lists[l] = head.next
            # merge L and R and put merged list into L
        
        mergeSortKListsRec(lists, 0, len(lists) - 1)
        if lists:
            return lists[0]
        else:
            return None
        

