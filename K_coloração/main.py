class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, value):
        self.vertices.append(value)
        self.edges[value] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.vertices:
            if vertex1 not in self.edges[vertex2] and vertex2 not in self.edges[vertex1]:
                self.edges[vertex1].append(vertex2)
                self.edges[vertex2].append(vertex1)

    def get_edges(self, value):
        if value in self.vertices:
            return self.edges[value]
        else:
            return False

    def get_all_edges(self):
        return self.edges


def graph_color(graph):
    max_colors = len(list(graph.keys()))
    graph_colors = {}
    for vertices in list(graph.keys()):
        graph_colors[vertices] = None

    for vertex in list(graph.keys()):
        vertex_edges = graph[vertex]
        graph_colors[vertex] = 1
        for edges in vertex_edges:
            if graph_colors[vertex] == graph_colors[edges]:
                graph_colors[vertex] = graph_colors[vertex] + 1
            else:
                pass

    return graph_colors

graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')

graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('a', 'e')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('b', 'f')
graph.add_edge('c', 'd')
graph.add_edge('c', 'f')
graph.add_edge('d', 'e')
graph.add_edge('d', 'f')

colors_graph = graph.get_all_edges()
print(graph_color(colors_graph))