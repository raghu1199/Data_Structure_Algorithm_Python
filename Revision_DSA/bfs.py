class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False


def bfs(node):
    print()
    if isinstance(node, Node):
        q = list()
        actual = node
        q.append(actual)

        while len(q) > 0:
            # first in first put->Queue
            actual = q.pop(0)
            print(f"{actual.name}->", end="")
            for neighbor in actual.adjacencyList:
                if not neighbor.visited:
                    neighbor.visited = True
                    q.append(neighbor)


def resetVisit(node):
    node.visited=False
    for n in node.adjacencyList:
        if n.visited:
            resetVisit(n)




def dfs(node):
    print()
    # reset visited mark to Not visited
    if isinstance(node,Node):
        stack=list()
        actual=node
        stack.append(actual)

        while len(stack)> 0:
            # last in first out ->stack
            actual=stack.pop(-1)
            print(f"{actual.name}->",end="")

            for neighbor in actual.adjacencyList:
                if not neighbor.visited:
                    neighbor.visited=True
                    stack.append(neighbor)




a=Node("A")
b=Node("B")
c=Node("C")
d=Node("D")
e=Node("E")
f=Node("F")
g=Node("G")
h=Node("H")
i=Node("I")
j=Node("J")
a.adjacencyList.append(b)
a.adjacencyList.append(c)
b.adjacencyList.append(d)
b.adjacencyList.append(e)
d.adjacencyList.append(f)
c.adjacencyList.append(g)
c.adjacencyList.append(h)
g.adjacencyList.append(i)
i.adjacencyList.append(j)

bfs(a)   # A->B->C->D->E->G->H->F->I->J->
resetVisit(a)
print()
print("All visited node has been Reset..")
dfs(a)   #
