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
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)

    def getMinvalue(self):
        if self.root:
            return self.__getMin(self.root)
        else:
            print("Tree is Empty")

    def __getMin(self,node):
        if node.leftchild:
            return self.__getMin(node.leftchild)
        else:
            return node.data

    def getMaxvalue(self):
        if self.root:
            return self.__getMax(self.root)
        else:
            print("tree is Empty")

    def __getMax(self,node):
        if node.rightchild:
            return self.__getMax(node.rightchild)
        else:
            return node.data

    def traverseInorder(self):
        if self.root:
            self.__inorder(self.root)
        print()

    def __inorder(self,node):
        if node.leftchild:
            self.__inorder(node.leftchild)

        print(f"{node.data}->",end="")

        if node.rightchild:
            self.__inorder(node.rightchild)

    def traversePreorder(self):
        if self.root:
            self.__preorder(self.root)
        else:
            print("Tree is Empty")
        print()

    def __preorder(self,node):

        print(f"{node.data}->",end="")
        if node.leftchild:
            self.__preorder(node.leftchild)
        if node.rightchild:
            self.__preorder(node.rightchild)

    def remove(self,data):
        if self.root:
            self.root=self.__removeNode(data,self.root)

    def __removeNode(self,data,node):

        if not node:
            return node
        #looking for node which has our data
        if data < node.data:
            node.leftchild=self.__removeNode(data,node.leftchild)
        elif data > node.data:
            node.rightchild=self.__removeNode(data,node.rightchild)

        # Now we found Node
        else:
            # node is single node ->leaf node (no any child)->update ref of parent node to none
            if not node.leftchild and not node.rightchild:
                print("Removing Leaf Node:")
                del node
                return None
            if not node.leftchild:
                print("Removing node with single rightchild")
                tempNode=node.rightchild
                del node
                return tempNode
            elif not node.rightchild:
                print("Removing node with single leftchild")
                tempNode=node.leftchild
                del node
                return tempNode

            print("removing Node with Two children")
            tempNode=self.getPredecessor(node.leftchild)
            node.data=tempNode.data
            node.leftchild=self.__removeNode(tempNode.data,node.leftchild)

        return node

    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node





b=BST()
b.insert(10)
b.insert(20)
b.insert(5)
b.insert(15)
b.insert(7)
b.insert(3)
b.insert(22)
b.insert(25)
b.insert(6)
print(b.getMaxvalue())
print(b.getMinvalue())
print(b.traverseInorder())
print(b.traversePreorder())
b.remove(22)
print(b.traverseInorder())
b.remove(7)
print(b.traverseInorder())
b.remove(10)
print(b.traverseInorder())



