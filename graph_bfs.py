class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.distance=9999
        self.visited=False
    # v is name of vertex
    def add_neighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            print(vertex.name, " is added to Graph")
            return True
        else:
            return False

    # u v are name of vertex
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbour(v)
                if key == v:
                    value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in list(self.vertices.keys()):
            print(f"{key}->{self.vertices[key].neighbours}")

    # vertex is Vertex object
    def breadthFirstSearch(self,vertex):
        q=[]
        vertex.distance=0
        vertex.visited=True
        print(vertex.name,end="->")
        for v in vertex.neighbours:
            self.vertices[v].distance=vertex.distance+1
            q.append(v)
        while len(q)>0:
            # get first inserted item in queue
            u=q.pop(0)
            node_u=self.vertices[u]
            node_u.visited=True
            print(node_u.name,end="->")
            for v in node_u.neighbours:
                node_v=self.vertices[v]
                if not node_v.visited:
                    q.append(v)
                    # default distance 9999
                    if node_v.distance > node_u.distance+1:
                        node_v.distance=node_u.distance+1



g=Graph()
a=Vertex("A")
g.add_vertex(a)
for i in range(ord("B"),ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges=["AB","AC","BD","BE","CG","CH","DF","HI","IJ"]
for edge in edges:
    u=edge[0]
    v=edge[1]
    g.add_edge(u,v)
g.print_graph()

g.breadthFirstSearch(a)