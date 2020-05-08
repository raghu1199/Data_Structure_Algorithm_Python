class Vertex:
    def __init__(self,name):
        self.name=name
        self.node=None


class Node:
    def __init__(self,height,nodeId,parentNode):
        self.height=height
        self.nodeId=nodeId
        self.parentNode=parentNode


class Edge:
    def __init__(self,weight,startVertex,targetVertex):
        self.weight=weight
        self.startVertex=startVertex
        self.targetVertex=targetVertex

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:
    def __init__(self,vertexList):
        self.vertexList=vertexList
        self.rootnodes=[]
        # makesets of each vertex at initilization of Disjoint
        self.makeSets(vertexList)

    def find(self,node):
        currentNode=node
        while currentNode.parentNode is not None:
            currentNode=currentNode.parentNode
        # we found root node assign to root and reinitialize currentNoe with given node
        root=currentNode
        currentNode=node
        # do path compression -> all node in that disjoint point to root direct
        while currentNode is not root:
            temp=currentNode.parentNode
            currentNode.parentNode=root
            currentNode=temp

        return root.nodeId

    def merge(self,node1,node2):
        index1=self.find(node1)
        index2=self.find(node2)
        # they are in same set do not merge
        if index1==index2:
            return
        root1=self.rootnodes[index1]
        root2=self.rootnodes[index2]

        if root1.height < root2.height:
            root1.parentNode=root2
        elif root1.height > root2.height:
            root2.parentNode=root1
        else:
            root2.parentNode=root1
            root1.height+=1

    def makeSets(self,vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self,vertex):
        node=Node(0,len(self.rootnodes),None)
        vertex.node=node
        self.rootnodes.append(node)


class KruskalAlgo:

    def spanningTree(self,vertexList,edgeList):
        cost=0
        disjointset=DisjointSet(vertexList)
        spannigTree=[]
        # sort is based on weight of Edges
        edgeList.sort()

        for edge in edgeList:
            u=edge.startVertex
            v=edge.targetVertex
            if disjointset.find(u.node) is not disjointset.find(v.node):
                spannigTree.append(edge)
                disjointset.merge(u.node,v.node)

        for edge in spannigTree:
            print(edge.startVertex.name,"<->",edge.targetVertex.name)
            cost+=edge.weight
        print("Total Minimum Cost is:", cost)

v1=Vertex("1")
v2=Vertex("2")
v3=Vertex("3")
v4=Vertex("4")

e12=Edge(5,v1,v2)
e23=Edge(3,v2,v3)
e34=Edge(6,v3,v4)
e41=Edge(4,v4,v1)
e42=Edge(2,v4,v2)

vertexList=[v1,v2,v3,v4]
edgeList=[e12,e23,e34,e41,e42]

al =KruskalAlgo()
al.spanningTree(vertexList,edgeList)

