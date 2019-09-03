from graph import Graph
from vertex import Vertex
#first connected graph
station_a = Vertex("a")
station_b = Vertex("b")
station_c = Vertex("c")
station_d = Vertex("d")
station_e = Vertex("e")
station_f = Vertex("f")
station_a1 = Vertex("a1")
station_a2 = Vertex("a2")
station_g = Vertex("g")

#second connected graph
station_a3 = Vertex("a3")
station_a4 = Vertex("a4")
station_a5 = Vertex("a5")
station_a6 = Vertex("a6")


my_railway = Graph()

my_railway.add_vertex(station_a)
my_railway.add_vertex(station_b)
my_railway.add_vertex(station_c)
my_railway.add_vertex(station_d)
my_railway.add_vertex(station_e)
my_railway.add_vertex(station_f)
my_railway.add_vertex(station_a1)
my_railway.add_vertex(station_g)
my_railway.add_vertex(station_a2)
my_railway.add_vertex(station_a3)
my_railway.add_vertex(station_a4)
my_railway.add_vertex(station_a5)
my_railway.add_vertex(station_a6)



my_railway.add_edge("a", "b", 3)
my_railway.add_edge("a", "c", 1)
my_railway.add_edge("c", "b", 1)
my_railway.add_edge("d", "b", 4)
my_railway.add_edge("d", "e", 1)
my_railway.add_edge("e", "f", 2)
my_railway.add_edge("c", "e", 2)
my_railway.add_edge("d", "f", 2)
my_railway.add_edge("f", "g", 2)
my_railway.add_edge("e", "a1", 2)
my_railway.add_edge("b", "e", 2)
my_railway.add_edge("f", "a1", 2)
my_railway.add_edge("g", "a1", 2)
my_railway.add_edge("a2", "a1", 2)

my_railway.add_edge("a3", "a4", 2)
my_railway.add_edge("a4", "a5", 2)
my_railway.add_edge("a5", "a6", 2)


while True:
    from_vertex = input("\n --- What's your starting point? ---\n")
    to_vertex = input("\n -- What's your end point? --\n")
    if my_railway.find_path(from_vertex, to_vertex):
        print("\n -- There's connection between vertices '{}' and '{}'! --\n".format(from_vertex, to_vertex))
    elif from_vertex not in my_railway.graph_dict or to_vertex not in my_railway.graph_dict:
        print("\n -- There are no such points in the graph --\n")
    else:
        print("\n -- There's no connection between vertices '{}' and '{}' --\n".format(from_vertex, to_vertex))
