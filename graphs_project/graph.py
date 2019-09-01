from vertex import Vertex

class Graph:

    def __init__(self, directed = False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding {}".format(vertex.vale))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from {} to {}".format(from_vertex.value, to_vertex.value))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
        if self.directed == False:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value)
