class Vertex:
    def __init__(self,name):
        self.name=name
        self.adjacencyList=list()

    def add_neighbor(self,v):
        if v not in self.adjacencyList:
            self.adjacencyList.append(v)


class Graph:
    vertices={}

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            print(f"{vertex.name} is Added to  vertices dict")
        else:
            print("Failed to Add")

    # u and v are name of verrtices not object itself
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key==u:
                    value.add_neighbor(v)
                if key==v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in list(self.vertices.keys()):
            print(key,"->",str(self.vertices[key].adjacencyList))

    def print_vertices(self):
        for key,value in self.vertices.items():
            print(f"{key}->{value.name}")

g=Graph()
g.add_vertex(Vertex("A"))
g.print_graph()

for i in range(ord("A"),ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges=["AB","AE","BF","CG","DE","EH","FG","FI","FJ","GJ","HI"]

for edge in edges:
    g.add_edge(edge[0],edge[1])

g.print_vertices()
g.print_graph()




