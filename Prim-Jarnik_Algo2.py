import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacencyList = []

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex




class PrimJarnik:

    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spannigTree = []
        self.edgeHeap = []
        self.fullCost = 0
        self.minList=[]
        self.minEdge=None

    def calculateSpanningTree(self, vertex):
        # [v1,v2,v3,v4]-> [v2,v3,v4]
        self.unvisitedList.remove(vertex)
        minEdge=vertex.adjacencyList[0]
        print(minEdge)
        while self.unvisitedList:
            # v1->e12,e13,e14
            for edge in vertex.adjacencyList:
                if edge.targetVertex in self.unvisitedList:
                    #heapq.heappush(self.edgeHeap, edge)
                    self.minList.append(edge)

            minEdge=self.minList[0]
            for edge in self.minList:
                if edge.weight < minEdge.weight:
                    minEdge=edge
            print(minEdge.weight)
            self.minList.remove(minEdge)
            #minEdge=heapq.heappop(self.edgeHeap)


            # e14 targetVertex is:v4
            if minEdge.targetVertex in self.unvisitedList:
                self.spannigTree.append(minEdge)
                print("Edge Added to Spanning tree:", minEdge.startVertex.name, "<->", minEdge.targetVertex.name)
                self.fullCost += minEdge.weight
                # store for next iteration V4-> start V4.adjacencyList
                vertex = minEdge.targetVertex
                # remove target v4 from list->[v2,v3,v4] ->[v2,v3]
                self.unvisitedList.remove(vertex)

        print("Total Min Cost of Spanning tree:", self.fullCost)


v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")

e12 = Edge(2, v1, v2)
e21 = Edge(2, v2, v1)
e13 = Edge(100, v1, v3)
e31 = Edge(100, v3, v1)
e14 = Edge(50, v1, v4)
e41 = Edge(50, v4, v1)
e34 = Edge(4, v3, v4)
e43 = Edge(4, v4, v3)
e24 = Edge(1, v2, v4)
e42 = Edge(1, v4, v2)

v1.adjacencyList.extend([e12, e13, e14])
v2.adjacencyList.extend([e21, e24])
v3.adjacencyList.extend([e31, e34])
v4.adjacencyList.extend([e41, e42, e43])

unvisitedlist = [v1, v2, v3, v4]
al = PrimJarnik(unvisitedlist)
al.calculateSpanningTree(v1)
