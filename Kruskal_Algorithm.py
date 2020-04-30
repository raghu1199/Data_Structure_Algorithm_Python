class Vertex:
    def __init__(self, name):
        self.name = name
        self.node = None


class Node:
    def __init__(self, height, nodeId, parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode


class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:
    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)


    def find(self, node):
        currentNode = node
        # find root first->root has parentNode None
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode

        # we found root node save it in root
        root = currentNode
        # take our node as currentNode again
        currentNode = node

        # path compression make all node.parent is->root
        while currentNode is not root:
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp

        return root.nodeId

    def merge(self, node1, node2):
        # get id of two different sets(Node)
        index1 = self.find(node1)
        index2 = self.find(node2)
        # if same id then they are in same disjoint not need to merge
        if index1 == index2:
            return

        # get root from list of rootNodes(sets) via id ->len(rootNodes) is assigned as id
        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        # small tree is attached to higher tree
        if root1.height < root2.height:
            root1.parentNode = root2
        elif root2.height < root1.height:
            root2.parentNode = root1
        # they are same height (A) (B) individual
        else:
            root2.parentNode = root1
            root1.height += 1

    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)
        vertex.node = node
        self.rootNodes.append(node)
        self.setCount += 1
        self.nodeCount += 1


class KruskalAlgorithm:

    def spanningTree(self, vertexList, edgeList):
        disjointset = DisjointSet(vertexList)
        spanningtree = []
        edgeList.sort()

        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex
            if disjointset.find(u.node) is not disjointset.find(v.node):
                spanningtree.append(edge)
                disjointset.merge(u.node, v.node)

        for edge in spanningtree:
            print(edge.startVertex.name, "<->", edge.targetVertex.name)


v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")
v5 = Vertex("E")
v6 = Vertex("F")
v7 = Vertex("G")

e1 = Edge(2, v1, v2)
e2 = Edge(6, v1, v3)
e3 = Edge(5, v1, v5)
e4 = Edge(10, v1, v6)
e5 = Edge(3, v2, v4)
e6 = Edge(3, v2, v5)
e7 = Edge(1, v3, v4)
e8 = Edge(2, v3, v6)
e9 = Edge(4, v4, v5)
e10 = Edge(5, v4, v7)
e11 = Edge(5, v6, v7)

vertexList = []
a = [v1, v2, v3, v4, v5, v6, v7]
vertexList.extend(a)
# print(vertexList)

edgeList = []
a = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]
edgeList.extend(a)
# print(edgeList)

al = KruskalAlgorithm()
al.spanningTree(vertexList, edgeList)
