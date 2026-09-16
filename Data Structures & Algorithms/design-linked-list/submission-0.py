class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        # Invalid index
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        i = 0
        while current != None:
            if i == index:
                return current.val
            current = current.next
            i = i + 1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        # is NOT the only node in the linked list
        if self.head is not None:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
        else:
            # is the firts node to be inserted
            # that's why we need to set self.tail as the new node as well
            self.head = newNode
            self.tail = newNode
            self.size += 1

        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is not None:
            self.tail.next = newNode 
            self.tail = newNode
            self.size += 1
        else:
            # is the firts node to be inserted
            # that's why we need to set self.tail as the new node as well
            self.head = newNode
            self.tail = newNode
            self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        newNode = Node(val)
        current = self.head
        i = 1
        while i < index:
            i += 1
            current = current.next
        newNode.next = current.next   
        current.next = newNode
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        # Invalid index
        if index < 0 or index >= self.size:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next

            # List became empty
            if self.head is None:
                self.tail = None

            self.size -= 1
            return

        # Find the node immediately before the target
        current = self.head
        i = 1

        while i < index:
            i += 1
            current = current.next

        # If target is the tail, update tail
        if current.next.next is None:
            self.tail = current

        # Remove target by bypassing it
        current.next = current.next.next

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)