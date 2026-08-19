class MyLinkedList:

    class ListNode:
        def __init__(self, val=0, nextNode=None):
            self.val = val
            self.nextNode = nextNode

    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        curr = self.head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.nextNode
        print(l)

    def get(self, index: int) -> int:
        
        curr = self.head
        currIndex = 0
        while curr:
            if index == currIndex:
                return curr.val
            curr = curr.nextNode
            currIndex +=1
        return -1

        

    def addAtHead(self, val: int) -> None:
        newHead = self.ListNode(val)

        if self.head:
            newHead.nextNode = self.head
            self.head = newHead


        else:
            self.head = newHead
            self.tail = newHead
        self.printList()


    def addAtTail(self, val: int) -> None:
        newTail = self.ListNode(val)

        if self.tail:
            self.tail.nextNode = newTail
            self.tail = newTail
        else:
            self.head = newTail
            self.tail = newTail
        self.printList()

    def addAtIndex(self, index: int, val: int) -> None:
        # if adding at index n, need n-1 -> next = newNode; newNode ->
        # next = n
        curr = self.head
        currIndex = 0

        newNode = self.ListNode(val)

        prevNode = None
        while curr:
            if index - 1 == currIndex:
                prevNode = curr
            curr = curr.nextNode
            currIndex +=1
        
        if prevNode:
            nxt = prevNode.nextNode
            # if no nextNode, moving the tail
            prevNode.nextNode = newNode
            newNode.nextNode = nxt
            if not nxt:
                self.tail = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        self.printList()

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        currIndex = 0

        prevNode = None
        currNode = None
        while curr:
            if index - 1 == currIndex:
                prevNode = curr
            if index == currIndex:
                currNode = curr
            curr = curr.nextNode
            currIndex +=1
        
        # to delete. need n-1, n, n+1 to link n-1 to n+1
        if prevNode and currNode:
            # if currNode.nextNode = None, prevNode becomes tail
            nxt = currNode.nextNode
            if not nxt:
                self.tail = prevNode
            prevNode.nextNode = nxt
        elif currNode:
            # currNode but no prevNode
            nxt = currNode.nextNode

            if not nxt:
                self.head = None
                self.tail = None
            else:
                self.head = nxt
        self.printList()




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)