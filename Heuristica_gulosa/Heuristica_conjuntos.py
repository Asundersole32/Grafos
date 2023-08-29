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

    def get_complementary(self):
        complementary = Graph()
        for i in self.vertices:
            complementary.add_vertex(i)

        for e in list(self.edges.keys()):
            for v in self.vertices:
                if v not in self.edges[e] and v != e:
                    complementary.add_edge(e, v)

        return complementary.get_all_edges()


def single_maximum_set(graph):
    vertices = list(graph.keys())
    independent_sets = []
    for i in vertices:
        clique = []
        clique.append(i)
        for v in vertices:
            if v in clique:
                continue
            is_next = True
            for u in clique:
                if u in graph[v]:
                    continue
                else:
                    is_next = False
                    break
            if is_next:
                clique.append(v)
        if clique not in independent_sets:
            independent_sets.append(clique)

    return independent_sets


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

maximum_set = single_maximum_set(graph.get_complementary())
print(maximum_set)
