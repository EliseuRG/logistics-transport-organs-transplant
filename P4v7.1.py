import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    "HD": {
        "HR": {"Ambulancia": 518, "Aviao": 460},
        "H4": {"Aviao": 42.5},
    },
    "H4": {
        "HR": {"Ambulancia": 1.6},
    },
    "HR": {},
}

G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=10, font_color='black', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

def dijkstra_multimodal(graph, start):
    distances = {node: {mode: float('infinity') for mode in graph[node]} for node in graph}
    distances[start] = {mode: 0 for mode in graph[start]}
    queue = [(0, start, mode) for mode in graph[start]]
    paths = {node: {mode: [] for mode in graph[node]} for node in graph}
    paths[start] = {mode: [start] for mode in graph[start]}

    while queue:
        current_distance, current_node, current_mode = heapq.heappop(queue)

        if current_distance > distances[current_node][current_mode]:
            continue

        for neighbor, weights in graph[current_node].items():
            if neighbor not in distances:
                continue
            for mode, weight in weights.items():
                if weight == 0:  # se a distância for zero, não inclua a rota
                    continue
                distance = current_distance + weight
                if distance < distances[neighbor].get(mode, float('infinity')):
                    distances[neighbor][mode] = distance
                    paths[neighbor][mode] = paths[current_node][current_mode] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor, mode))

    return distances, paths

# Execute a função para cada segmento da viagem
distances, paths = dijkstra_multimodal(graph, "HD")

# Encontre o percurso com a menor distância total
min_distance = float('infinity')
min_path = None
min_mode = None
for node, modes in distances.items():
    if node == "HD":  # ignore o nó inicial
        continue
    for mode, distance in modes.items():
        if distance < min_distance:
            min_distance = distance
            min_path = paths[node][mode]
            min_mode = mode

# Imprima os detalhes do melhor percurso
if min_path is not None:
    print(f"Melhor percurso: {' > '.join(min_path)}")
    print(f"Transbordos: {min_mode}")
    print(f"Distância: {min_distance} Km")
else:
    print("Nenhum percurso encontrado.")