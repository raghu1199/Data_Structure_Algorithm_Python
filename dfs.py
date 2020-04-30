class Node:
    def __init__(self,name):
        self.name=name
        self.neighbors=[]
        self.visited=False

class BFS:

    def bfs(self,node):
        q = list()
        actual=node
        q.append(actual)
        while len(q)>0:
            actual=q.pop(-1)
            print(actual.name,"->",end="")
            for v in actual.neighbors:
                if not v.visited:
                    v.visited=True
                    q.append(v)

n1=Node("A")
n2=Node("B")
n3=Node("C")
n4=Node("D")
n5=Node("E")
n6=Node("F")
n7=Node("G")
n8=Node("H")
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n4)
n3.neighbors.append(n6)
n4.neighbors.append(n5)
n6.neighbors.append(n7)
n5.neighbors.append(n8)
b=BFS()
b.bfs(n1)



