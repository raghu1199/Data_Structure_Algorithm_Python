import heapq


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = 9999

    def __lt__(self, other):
        return self.minDistance < other.minDistance


class Edge:
    def __init__(self,weight,startVertex,targetVertex):
        self.weight=weight
        self.startVertex=startVertex
        self.targetVertex=targetVertex


class Algorithm:

    def calculateShortestPath(self,startVertex):
        q_heap=[]
        startVertex.minDistance=0
        heapq.heappush(q_heap,startVertex)
        while len(q_heap)>0:
            # returns having minDistance Vertex
            currentVertex = heapq.heappop(q_heap)

            for edge in currentVertex.adjacencyList:
                u=edge.startVertex
                v=edge.targetVertex
                newDistance = u.minDistance+edge.weight
                if newDistance < v.minDistance:
                    v.minDistance=newDistance
                    v.predecessor=u
                    heapq.heappush(q_heap,v)

    def getShortestPath(self,targetVertex):
        print("Shortest Path to Vertex:",targetVertex.name," is:",targetVertex.minDistance)
        currentNode=targetVertex
        print(f"{currentNode.name}->",end="")
        while currentNode.predecessor is not None:
            currentNode = currentNode.predecessor
            print(f"{currentNode.name}->",end="")


n1=Node("1")
n2=Node("2")
n3=Node("3")
n4=Node("4")
n5=Node("5")
n6=Node("6")

e12=Edge(2,n1,n2)
e13=Edge(4,n1,n3)
e24=Edge(7,n2,n4)
e23=Edge(1,n2,n3)
e35=Edge(3,n3,n5)
e56=Edge(5,n5,n6)
e54=Edge(2,n5,n4)
e46=Edge(1,n4,n6)

n1.adjacencyList.extend([e12,e13])
n2.adjacencyList.extend([e24,e23])
n3.adjacencyList.append(e35)
n4.adjacencyList.append(e46)
n5.adjacencyList.extend([e54,e56])

al=Algorithm()
al.calculateShortestPath(n1)
al.getShortestPath(n4)





