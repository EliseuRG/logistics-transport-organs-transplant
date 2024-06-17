import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    "HD": {
        "HR": {"Ambulancia" : 518,   "Helicoptero": 460},
        "A1": {"Ambulancia" : 12.05, "Helicoptero": 13.6},
        "H1": {"Ambulancia" : 3.6},
        "H2": {"Helicoptero": 2.76},
        "H4": {"Helicoptero": 462.5},
    },
    "H1": {
        "HR": {"Helicoptero": 458},
        "A1": {"Helicoptero": 9.55},
        "H2": {"Helicoptero": 9.55},
        "H4": {"Helicoptero": 457},
    },
    "H2": {
        "A1": {"Ambulancia": 10.7},
    },
    "H3": {
        "HR": {"Helicoptero": 741},
        "H4": {"Helicoptero": 6.7},
    },
    "H4": {
        "HR": {"Ambulancia": 1.6},
    },
    "A1": {
        "A2": {"Aviao": 469},
    },
    "A2": {
        "HR": {"Ambulancia" : 10,   "Helicoptero": 12.7},
        "H3": {"Ambulancia" : 58},
        "H4": {"Helicoptero": 8.76},
    },
    "HR": {},
}

G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=10, font_color='black', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

def dijkstra_multimodal(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start, '')]
    paths = {node: [] for node in graph}
    paths[start] = [start]
    modes = {node: [] for node in graph}

    while queue:
        current_distance, current_node, current_mode = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weights in graph[current_node].items():
            for mode, weight in weights.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_node] + [neighbor]
                    modes[neighbor] = modes[current_node] + [mode] if current_mode != mode else modes[current_node]
                    heapq.heappush(queue, (distance, neighbor, mode))

    return distances[end], paths[end], modes[end]

# Execute a função para cada segmento da viagem
distance, path, mode = dijkstra_multimodal(graph, "HD", "HR")

# Imprima os detalhes do melhor percurso
if path is not None:
    print(f"Melhor percurso: {' > '.join(path)}")
    print(f"Transbordos....: {' > '.join(mode)}")
    print(f"Distância......: {distance} Km")
else:
    print("Nenhum percurso encontrado.")