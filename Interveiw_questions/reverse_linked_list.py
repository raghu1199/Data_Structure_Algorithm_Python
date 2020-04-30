class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # fast_pointer traverses list 2x than slow_pointer ->so middle element in-> slow_pointer.data
    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer.data

    # Reverse traverseList
    def reverse(self):
        current=self.head
        prev=None
        next=None

        while current is not None:
            next = current.nextNode
            current.nextNode = prev
            prev=current
            current = next

        self.head = prev





    def traverseList(self):
        currentNode=self.head

        while currentNode is not None:
            print(f"{currentNode.data}->",end="")
            currentNode=currentNode.nextNode
        print()


linked=LinkedList()
linked.insertStart(12)
linked.insertStart(122)
linked.insertStart(3)
linked.insertStart(31)
linked.insertStart(10)
linked.insertStart(11)
linked.insertStart(26)
linked.insertStart(32)
linked.insertStart(50)
linked.traverseList()
print(linked.get_middle_node())
linked.reverse()
linked.traverseList()