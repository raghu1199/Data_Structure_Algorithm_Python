class Node:
    def __init__(self,data):
        self.data=data
        self.height=0
        self.leftchild=None
        self.rightchild=None


class AVL:
    def __init__(self):
        self.root=None

    def calcHeight(self,node):
        if not node:
            return -1
        return node.height

    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftchild)-self.calcHeight(node.rightchild)

    def rotateRight(self,node):
        print("Rotating Right On node:",node.data)
        tempLeft=node.leftchild
        t=tempLeft.rightchild

        tempLeft.rightchild=node
        node.leftchild=t

        node.height=max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1
        tempLeft.height=max(self.calcHeight(tempLeft.leftchild),self.calcHeight(tempLeft.rightchild))+1

        return tempLeft

    def rotateLeft(self,node):
        print("Rotating Left On Node:",node.data)
        tempRight=node.rightchild
        t=tempRight.leftchild

        tempRight.leftchild=node
        node.rightchild=t

        node.height=max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1
        tempRight.height=max(self.calcHeight(tempRight.leftchild),self.calcHeight(tempRight.rightchild))+1

        return tempRight

    def insert(self,data):
        self.root=self.__insertNode(data,self.root)

    def __insertNode(self,data,node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftchild=self.__insertNode(data,node.leftchild)
        else:
            node.rightchild=self.__insertNode(data,node.rightchild)

        node.height=max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1

        return self.__settleViolation(data,node)

    def __settleViolation(self,data,node):
        balance=self.calcBalance(node)

        if balance > 1 and data < node.leftchild.data:
            print("Left left heavy Situation..")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightchild.data:
            print("Right Right Heavy Situation..")
            return self.rotateLeft(node)

        if balance >1 and data > node.leftchild.data:
            print("LEFT RIGHT situaiton..")
            node.leftchild=self.rotateLeft(node.leftchild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightchild.data:
            print("RIght LEft situation..")
            node.rightchild=self.rotateRight(node.rightchild)
            return self.rotateLeft(node)

        return node

    def traverse(self):
        print()
        if self.root:
            self.__inOrder(self.root)

    def __inOrder(self,node):
        if node.leftchild:
            self.__inOrder(node.leftchild)

        print(f"{node.data}->",end=" ")

        if node.rightchild:
            self.__inOrder(node.rightchild)


avl=AVL()
avl.insert(5)
avl.insert(7)
avl.insert(8)
avl.traverse()

