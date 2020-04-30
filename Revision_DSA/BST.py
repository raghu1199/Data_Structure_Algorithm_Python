class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.__insertNode(data,self.root)

    def __insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self.__insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.__insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)

    # with return so print(b.getMinValue())
    def getMinValue(self):
        if self.root:
            return self.__getMin(self.root)
        else:
            print("tree is Empty")

    def __getMin(self,node):
        if node.leftchild:
            return self.__getMin(node.leftchild)
        else:
            return node.data

    # without return so just b.getMaxValue
    def getMaxValue(self):
        if self.root:
            self.__getMax(self.root)
        else:
            print("Treee is Empty")

    def __getMax(self,node):
        if node.rightchild:
            self.__getMax(node.rightchild)
        else:
            print(node.data)

    def traverse(self):
        if self.root:
            self.__inorder(self.root)
        else:
            print("Tree is Empty")

    def __inorder(self,node):

        if node.leftchild:
            self.__inorder(node.leftchild)

        print(f"{node.data}->",end="")

        if node.rightchild:
            self.__inorder(node.rightchild)

    def remove(self,data):
        print()
        if self.root:
            self.root=self.__removeNode(data,self.root)

    def __removeNode(self,data,node):
        if data < node.data:
            node.leftchild=self.__removeNode(data,node.leftchild)
        elif data > node.data:
            node.rightchild=self.__removeNode(data,node.rightchild)

        # we found Node data=node.data
        else:
            if not node.leftchild and not node.rightchild:
                print("Removing Leaf node which doesnot have any child")
                del node
                return None

            elif not node.leftchild:
                print("Removing node with single Right child only..")
                tempNode=node.rightchild
                del node
                return tempNode

            elif not node.rightchild:
                print("Removing node with single leftchild only")
                tempNode=node.leftchild
                del node
                return tempNode

            print("Removing node with Two children..")
            tempNode=self.__getpredecessor(node.leftchild)
            print("Before Swap node.data:", node.data, "tempnode.data:", tempNode.data)
            node.data,tempNode.data = tempNode.data, node.data
            print("After swap node.data:",node.data,"tempnode.data:",tempNode.data)

            node.leftchild=self.__removeNode(tempNode.data,node.leftchild)

        return node

    def __getpredecessor(self,node):
        if node.rightchild:
            return self.__getpredecessor(node.rightchild)
        return node





b=BST()
b.traverse()
b.getMaxValue()
b.getMinValue()

b.insert(20)
b.insert(30)
b.insert(15)
b.insert(16)
b.insert(13)
b.insert(28)
b.insert(32)
b.insert(31)
b.insert(14)
print(b.getMinValue())
b.getMaxValue()
b.traverse()
b.remove(16)
b.traverse()
b.remove(13)
b.traverse()
b.remove(32)
b.traverse()
b.remove(20)
b.traverse()
