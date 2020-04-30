class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtStart(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size1(self):
        return self.size

    def size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    def insertAtEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def insertAtPosition(self, data, req_pos):
        current_pos = 0
        currentNode = self.head
        prevNode = None
        newNode = Node(data)
        self.size += 1

        while current_pos != req_pos:
            prevNode = currentNode
            currentNode = currentNode.nextNode
            current_pos += 1

        newNode.nextNode = currentNode
        prevNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print(f"{actualNode.data} ->", end="")
            actualNode = actualNode.nextNode
        print()

    def remove(self, data):
        if self.head is None:
            print("LinkedList is Empty")
            return

        self.size -= 1
        currentNode = self.head
        prevNode = None
        while currentNode.data != data:
            prevNode = currentNode
            currentNode = currentNode.nextNode
        # for only one element present(head)
        if prevNode is None:
            self.head = currentNode.nextNode
        else:
            prevNode.nextNode = currentNode.nextNode


link = LinkedList()
print(link.size1())
link.insertAtStart(10)
link.insertAtStart(5)
link.insertAtStart(0)
print(link.size1())
link.insertAtEnd(50)
link.traverseList()
link.remove(10)
link.traverseList()
link.insertAtPosition(10,1)
link.traverseList()
print(link.size1())
