class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            # self.neighbors.name.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            print(f"vertex:{vertex.name} is added to graph")
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                print(f"key is:{key} value:{value}")
                if key == u:
                    value.add_neighbor(v)
                    print(f"{v} is added as neighbor in {key},-> Neighbors of {key} are:{value.neighbors}")
                if key == v:
                    value.add_neighbor(u)
                    print(f"{u} is added as neighbor in {key}-> Neighbors of {key} are:{value.neighbors}")
            return True
        else:
            return False

    def print_graph(self):
        print("Graph is:")
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors))


g = Graph()
a = Vertex("A")
b = Vertex("B")
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(Vertex("C"))
g.add_vertex(Vertex("D"))
g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")

print(g.vertices)
g.print_graph()

"""
a=Vertex("A")
a.add_neighbor(Vertex(5))
a.add_neighbor(Vertex(7))
for neighbor in a.neighbors:
    print(neighbor.name)
"""
