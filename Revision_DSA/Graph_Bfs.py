class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.distance = 9999
        self.visited = False

    def add_neighbor(self, v):
        if v not in self.adjacencyList:
            self.adjacencyList.append(v)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

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
            print(f"{key}->{self.vertices[key].adjacencyList}")

    def bfs(self,vert):
        q=list()
        vert.distance=0
        q.append(vert.name)

        while len(q)>0:
            # get first item
            u = q.pop(0)

            # get vertex object from vertices dict
            vertex_u=self.vertices[u]
            vertex_u.visited=True

            print(f"{vertex_u.name} {vertex_u.distance}->",end="")

            for v in vertex_u.adjacencyList:
                vertex_v=self.vertices[v]
                vertex_v.distance=vertex_u.distance+1
                if not vertex_v.visited:
                    q.append(v)


g=Graph()
a=Vertex("A")
g.add_vertex(a)
for i in range(ord("A"),ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges=["AB","AC","BD","BE","DF","CG","CH","HI","IJ"]

for edge in edges:
    g.add_edge(edge[0],edge[1])

g.bfs(a)  # A->B->C->D->E->G->H->F->I->J->



