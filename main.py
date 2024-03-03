import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

### МАПА
kyiv_map = {
    "Майдан_Незалежности": {
        "Хрещатик": 3.5, 
        "Собор_Святої_Софії": 2.1, 
        "Лавра": 2.3
        },
    "Хрещатик": {
        "Майдан_Незалежности": 3.5,
        "Володимирський_Собор": 4.2,
        "Узвіз": 1.2,
    },
    "Володимирський_Собор": {
        "Хрещатик": 4.2,
        "Собор_Святої_Софії": 4.6,
        "Історичний_Музей": 2.7,
        "Узвіз": 3.0,
    },
    "Собор_Святої_Софії": {
        "Майдан_Незалежности": 2.1, 
        "Володимирський_Собор": 4.6
        },
    "Лавра": {
        "Майдан_Незалежности": 2.3
        },
    "Історичний_Музей": {
        "Володимирський_Собор": 2.7
        },
    "Узвіз": {
        "Хрещатик": 1.2, 
        "Володимирський_Собор": 3.0
        },
}

### ПОШУК У ШИРИНУ (BFS)
def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs(graph, queue, visited)

### ПОШУК У ГЛИБИНУ (DFS)
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

### ДЕЙКСТРА
def dijkstra(graph: dict, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = round(distance, 2)

        unvisited.remove(current_vertex)

    return distances


### ЗАВДАННЯ 1
graph = nx.Graph()

for node, neighbors in kyiv_map.items():
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight)

print("\n>>>КІЛЬКІСТЬ ВЕРШИН: \n", graph.number_of_nodes())
print("\n>>>КІЛЬКІСТЬ РЕБЕР: \n", graph.number_of_edges())
print("\n>>>СПИСОК ВЕРШИН: \n", list(graph.nodes()))
print("\n>>>СПИСОК РЕБЕР: \n", list(graph.edges()))
print("\n>>>РІВЕНЬ ВЕРШИН: \n", dict(graph.degree()))

pos = nx.shell_layout(graph)
nx.draw(
    graph,
    pos,
    with_labels=True,
    node_color="green",
)

edge_weights = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(
    graph, pos, edge_labels=edge_weights
)

start = "Історичний_Музей"

### ЗАВДАННЯ 2
print("\n>>>ПОШУК У ГЛИБИНУ (DFS):")
dfs(graph, start)

print("\n\n>>>ПОШУК У ШИРИНУ (BFS):")
bfs(graph, deque([start]))

### ЗАВДАННЯ 3
print("\n\n>>>ДЕЙКСТРА:")
print(dijkstra(kyiv_map, start))

plt.show()
