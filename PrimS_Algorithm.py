import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex=startVertex
        self.targetVertex=targetVertex

    def __cmp__(self, other):
        return self.cmp(self.weight,other.weight)

    def __lt__(self,other):
        return self.weight < other.weight


class PrimsJarnik:

    def __init__(self,unvisitedList):
        self.unvisitedList=unvisitedList
        self.spanningTree=[]
        self.edgeHeap=[]
        self.fullcost=0

    def calculateSpanningTree(self,vertex):
        self.unvisitedList.remove(vertex)

        while self.unvisitedList:
            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)

            minEdge=heapq.heappop(self.edgeHeap)
            if minEdge.targetVertex in self.unvisitedList:
                self.spanningTree.append(minEdge)
                print("Edge added to spanning tree:",minEdge.startVertex,"<->",minEdge.targetVertex)
                self.fullcost+=minEdge.weight
                # update vertex for next finding adjacencyList
                vertex=minEdge.targetVertex
                # remove visited vertex
                self.unvisitedList.remove(vertex)

    def getCost(self):
        return self.fullcost





v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")

e12=Edge(1,v1,v2)
e21=Edge(1,v2,v1)
e13=Edge(10,v1,v3)
e31=Edge(10,v3,v1)
e34=Edge(4,v3,v4)
e43=Edge(4,v4,v3)
e14=Edge(0,v1,v4)
e41=Edge(0,v4,v1)
e42=Edge(3,v4,v2)
e24=Edge(3,v2,v4)


v1.adjacencyList.extend([e12,e31,e14])
v2.adjacencyList.extend([e21,e24])
v4.adjacencyList.extend([e41,e42,e43])
v3.adjacencyList.extend([e31,e34])

unvisitedList=[v1,v2,v3,v4]

al=PrimsJarnik(unvisitedList)
al.calculateSpanningTree(v3)
print(al.getCost())


