class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.distance = 9999
        self.color = "black"

    def add_neighbor(self, v):
        # v is name of vertex not Object
        if v not in self.neighbors:
            self.neighbors.append(v)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            print(f"vertex:{vertex.name} is added to vertices ->now vertices:{self.vertices}")
            return True
        else:
            return False

    # u and v are name of vertex
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == v:
                    value.add_neighbor(u)
                    print(f"{u} is added to neighbor list {value.name},->Neighbors:{value.neighbors}")
                if key == u:
                    value.add_neighbor(v)
                    print(f"{v} is added to neighbor list {value.name}->Neighbors:{value.neighbors}")
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors)+" "+str(self.vertices[key].distance)+" "+str(self.vertices[key].color))

    def bfs(self,vert):
        print("Visiting ....")
        q=list()
        vert.distance=0
        vert.color="red"
        print(f"{vert.name} neighbors are:{vert.neighbors}")
        for v in vert.neighbors:
            self.vertices[v].distance=vert.distance+1
            q.append(v)

        while len(q)>0:
            print()
            print("queue:", q,"popin first item..")
            u=q.pop(0)

            node_u=self.vertices[u]
            node_u.color="red"
            print("parent:",node_u.name,"->",end="")
            print(f"{node_u.name} neighbors are:{node_u.neighbors}")
            for v in node_u.neighbors:
                node_v=self.vertices[v]
                print("neigbors:",node_v.name,"->",end="")
                if node_v.color=="black":
                    q.append(v)
                    if node_v.distance > node_u.distance+1:
                        node_v.distance=node_u.distance+1
                print()

g=Graph()
a=Vertex("A")
g.add_vertex(a)
for i in range(ord('A'),ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges=['AB','AE','BF','CG','DE','DH','EH','FG','FI','FJ','GJ','HI']
for edge in edges:
    g.add_edge(edge[:1],edge[1:])

g.bfs(a)
g.print_graph()