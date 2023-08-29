import sys


def dijkstra(graph, origin):

  distance = {v: sys.maxsize for v in graph}
  distance[origin] = 0

  visited = set()

  while visited != set(distance):
      actual_vertex = None
      shortest_distance = sys.maxsize
      for v in graph:
          if v not in visited and distance[v] < shortest_distance:
              actual_vertex = v
              shortest_distance = distance[v]

      visited.add(actual_vertex)

      for neighbor, weight in graph[actual_vertex].items():
          if distance[actual_vertex] + weight < distance[neighbor]:
              distance[neighbor] = distance[actual_vertex] + weight

  return distance

graph = {
    '0': {'1': 4, '7': 8},
    '1': {'0': 4, '2': 8, '7': 11},
    '2': {'1': 8, '3': 7, '5': 4, '8': 2},
    '3': {'2': 7, '4': 9, '5': 14},
    '4': {'3': 9, '5': 10},
    '5': {'2': 4, '3': 14, '4': 10, '6': 2},
    '6': {'5': 2, '7': 1, '8': 6},
    '7': {'0': 8, '1': 11, '6': 1, '8': 7},
    '8': {'2': 2, '6': 6, '7': 7}
}


origin = '0'

shortest_path = dijkstra(graph, origin)

for destiny, distance in shortest_path.items():
  print(f"Caminho mais curto de {origin} para {destiny}: {distance}")