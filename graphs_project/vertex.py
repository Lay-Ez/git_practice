
class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex):
        print("Adding edge to {}".format(vertex))
        self.edges[vertex] = True
        
