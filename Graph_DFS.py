class Node:
    def __init__(self,name):
        self.name=name
        self.neighbors=[]
        self.visited=False

class DFS:
    def dfs(self,node):
        node.visited=True
        print(f"node:{node.name} visted:{node.visited} adjacents:")
        for n in node.neighbors:
            if not n.visited:
                self.dfs(n)

n1=Node("A")
n2=Node("B")
n3=Node("C")
n4=Node("D")
n5=Node("E")
n6=Node("F")
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n4)
n3.neighbors.append(n6)
n4.neighbors.append(n5)

d=DFS()
d.dfs(n1)

