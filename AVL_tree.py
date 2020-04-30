class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftchild = None
        self.rightchild = None


class AVL:
    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftchild) - self.calcHeight(node.rightchild)

    # left heavy situation
    def rotateRight(self, node):
        print("Rotating to right on Node:", node.data)
        templeftChild = node.leftchild
        t = templeftChild.rightchild

        templeftChild.rightchild = node
        node.leftchild = t

        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        templeftChild.height = max(self.calcHeight(templeftChild.leftchild),
                                   self.calcHeight(templeftChild.rightchild)) + 1

        return templeftChild

    def rotateLeft(self, node):
        print("Rotating Left on Node:", node)
        temprightChild = node.rightchild
        t = temprightChild.leftchild

        temprightChild.leftchild = node
        node.rightchild = t

        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        temprightChild.height = max(self.calcHeight(temprightChild.leftchild),
                                    self.calcHeight(temprightChild.rightchild)) + 1

        return temprightChild

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftchild = self.insertNode(data, node.leftchild)
        else:
            node.rightchild = self.insertNode(data, node.rightchild)

        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        return self.setViolation(data, node)

    def setViolation(self, data, node):
        balance = self.calcBalance(node)

        # case 1 left left heavy situation
        if balance > 1 and data < node.leftchild.data:
            print("Left Left heavy Situation..")
            return self.rotateRight(node)

        # case 2 right right heavy situation
        if balance < -1 and data > node.rightchild.data:
            print("Right Right Heavy situation..")
            return self.rotateLeft(node)

        # case 3 left right situation
        if balance > 1 and data > node.leftchild.data:
            print("Left right Situation..")
            node.leftchild = self.rotateLeft(node.leftchild)
            return self.rotateRight(node)
        # case 4 right left situation
        if balance < -1 and data < node.rightchild.data:
            print("Right Left Situation..")
            node.rightchild = self.rotateRight(node.rightchild)
            return self.rotateLeft(node)

        return node

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
            print()
        else:
            print("AVL tree is Empty")

    def traverseInorder(self, node):
        if node.leftchild:
            self.traverseInorder(node.leftchild)

        print(node.data, "->", end="")

        if node.rightchild:
            self.traverseInorder(node.rightchild)

avl=AVL()
"""
# left left heavy
avl.insert(5)
avl.insert(4)
avl.insert(3)
avl.traverse()"""

"""
# right right heavy
avl.insert(5)
avl.insert(6)
avl.insert(7)
avl.traverse() """
"""
avl.insert(5)
avl.insert(3)
avl.insert(4)
avl.traverse()
"""

avl.insert(5)
avl.insert(7)
avl.insert(6)
avl.traverse()


