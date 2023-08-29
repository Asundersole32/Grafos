from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)


g = Graph(10)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(0, 2)
g.addEdge(0, 5)
g.addEdge(5, 6)
g.addEdge(5, 4)
g.addEdge(9, 6)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(1, 2)
g.addEdge(4, 6)
g.addEdge(6, 7)
g.addEdge(6, 8)
g.addEdge(7, 8)

print("Ordenação topologica do grafo:")
g.topologicalSort()