class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.visited = False
        self.predecessor = None


def dfs(node):
    if isinstance(node, Node):
        node.visited = True
        print(f"{node.name}->",end="")

        for neighbor in node.neighbors:
            if not neighbor.visited:
                dfs(neighbor)

a=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")
e=Node("E")
f=Node("F")
g=Node("G")
a.neighbors.append(b)
a.neighbors.append(c)
b.neighbors.append(d)
b.neighbors.append(e)
d.neighbors.append(f)
c.neighbors.append(g)

dfs(a)  #A->B->D->F->E->C->G->


