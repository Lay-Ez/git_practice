from vertex import Vertex

class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding vertex: '{}'".format(vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        try:
            print("Adding edge from '{}' to '{}'".format(from_vertex.value, to_vertex.value))
            self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
            if self.directed == False:
                self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
        except AttributeError:
            print("Adding edge from '{}' to '{}'".format(from_vertex, to_vertex))
            self.graph_dict[from_vertex].add_edge(to_vertex, weight)
            if self.directed == False:
                self.graph_dict[to_vertex].add_edge(from_vertex, weight)


    def find_path(self, start_vertex, end_vertex):
        print("Searching for path from '{}' to '{}'".format(start_vertex, end_vertex))
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print(current_vertex)
            if current_vertex == end_vertex:
                return True
            vertex = self.graph_dict[current_vertex]
            next_vertices = vertex.get_edges()
            next_vertices = [vertex for vertex in next_vertices if vertex not in seen and vertex not in start]
            start.extend(next_vertices)
        return False
