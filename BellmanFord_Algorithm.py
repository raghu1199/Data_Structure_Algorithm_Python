import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.minDistance = sys.maxsize


class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


class BallmanFord:
    HAS_CYCLE = False

    def calculateShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDistance = 0

        for i in range(0, len(vertexList) - 1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
                print("Negative Cycle Detected at..", edge)
                BallmanFord.HAS_CYCLE = True
                return

    def getShortestPath(self, targetVertex):
        if not BallmanFord.HAS_CYCLE:
            print("Shortest path:", targetVertex.minDistance)
            node = targetVertex
            while node is not None:
                print(f"{node.name}->")
                node = node.predecessor
        else:
            print("Shortest path has extra Negative cycle")


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e1 = Edge(2, a, b)
e2 = Edge(1, b, c)
e3 = Edge(-4, c, d)
e4 = Edge(1, d, a)

edgeList = (e1, e2, e3, e4)
VertexList = (a, b, c, d)

al = BallmanFord()
al.calculateShortestPath(VertexList, edgeList, a)
al.getShortestPath(d)
