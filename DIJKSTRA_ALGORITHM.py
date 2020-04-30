import sys
import heapq


class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
    """
    def __cmp__(self, other):
        return self.cmp(self.minDistance, other.minDistance)"""

    def __lt__(self, other):
        return self.minDistance < other.minDistance


class Algorithm:

    def calculateShortestPath(self, startVertex):
        q = []
        startVertex.minDistance = 0
        heapq.heappush(q,startVertex)
        while len(q)>0:
            actualVertex=heapq.heappop(q)
            for edge in actualVertex.adjacenciesList:
                u=edge.startVertex
                v=edge.targetVertex
                newDistance=u.minDistance+edge.weight
                if newDistance < v.minDistance:
                    v.predecessor=u
                    v.minDistance=newDistance
                    heapq.heappush(q,v)

    def getShortestPath(self,targetVertex):
        print("shortest path to vertex:",targetVertex.minDistance)
        node=targetVertex
        while node is not None:
            print(f"{node.name}->",end=" ")
            node=node.predecessor

n1=Node("A")
n2=Node("B")
n3=Node("C")
n4=Node("D")
n5=Node("E")
n6=Node("F")
n7=Node("G")
n8=Node("H")

e1=Edge(5,n1,n2)
e2=Edge(8,n1,n8)
e3=Edge(9,n1,n5)
e4=Edge(15,n2,n4)
e5=Edge(12,n2,n3)
e6=Edge(4,n2,n8)
e7=Edge(7,n8,n3)
e8=Edge(6,n8,n6)
e9=Edge(5,n5,n8)
e10=Edge(4,n5,n6)
e11=Edge(20,n5,n7)
e12=Edge(1,n6,n3)
e13=Edge(13,n6,n7)
e14=Edge(3,n3,n4)
e15=Edge(11,n3,n7)
e16=Edge(9,n4,n7)

n1.adjacenciesList.append(e1)
n1.adjacenciesList.append(e2)
n1.adjacenciesList.append(e3)
n2.adjacenciesList.append(e4)
n2.adjacenciesList.append(e5)
n2.adjacenciesList.append(e6)
n8.adjacenciesList.append(e7)
n8.adjacenciesList.append(e8)
n5.adjacenciesList.append(e9)
n5.adjacenciesList.append(e10)
n5.adjacenciesList.append(e11)
n6.adjacenciesList.append(e12)
n6.adjacenciesList.append(e13)
n3.adjacenciesList.append(e14)
n3.adjacenciesList.append(e15)
n4.adjacenciesList.append(e16)

al=Algorithm()
al.calculateShortestPath(n1)
al.getShortestPath(n7)










