class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, origin, destination, weight):
        self.origin = origin
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)
        edge.origin.edges.append(edge)

def create_graph(data):
    graph = Graph()
    for i in range(0, len(data), 30):
        origin = Node(i)
        graph.add_node(origin)
        if i + 2 < len(data) and data[i+1] is not None and data[i+2] is not None:
            destination = Node(i+2)
            weight = data[i+1]
            graph.add_node(destination)
            edge = Edge(origin, destination, weight)
            graph.add_edge(edge)
    return graph

def shortest_path(graph, start, end):
    unvisited_nodes = list(graph.nodes)
    shortest_distances = {node: float('inf') for node in graph.nodes}
    shortest_distances[start] = 0
    current_node = start
    while current_node != end:
        for edge in current_node.edges:
            if edge.destination in unvisited_nodes:
                new_distance = shortest_distances[current_node] + edge.weight
                if new_distance < shortest_distances[edge.destination]:
                    shortest_distances[edge.destination] = new_distance
        unvisited_nodes.remove(current_node)
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])
    return shortest_distances[end]

def main():
    data = [
        [0.02, 5.755556, 0.02, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, 0.25, 1.84, 0.25, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 1.832, 0.25, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, 0.25, 1.85, 0.25, 0.02, 0.035556, 0.02, None, None, None, None, None, None, None, None, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 1.828, 0.25, 0.02, 0.035556, 0.02, None, None, None, None, None, None, None, None, None, None, None],
        [0.02, 0.30222, 0.02, None, None, None, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None],
        [0.02, 0.30222, 0.02, None, None, None, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.04, 0.25, None, None, None],
        [0.02, 0.30222, 0.02, None, None, None, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None, None],
        [0.02, 0.30222, 0.02, None, None, None, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.03504, 0.25, 0.02, 0.035556, 0.02],
        [0.02, 0.30222, 0.02, None, None, None, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.0268, 0.25, 0.02, 0.035556, 0.02],
        [None, None, None, 0.25, 0.0482, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None],
        [None, None, None, 0.25, 0.0482, 0.25, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.04, 0.25, None, None, None],
        [None, None, None, 0.25, 0.0482, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None, None],
        [None, None, None, 0.25, 0.0482, 0.25, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.03504, 0.25, 0.02, 0.035556, 0.02],
        [None, None, None, 0.25, 0.0482, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.0268, 0.25, 0.02, 0.035556, 0.02],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.04, 0.25, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, None, None, None, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.03504, 0.25, 0.02, 0.035556, 0.02],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, None, None, None, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.0268, 0.25, 0.02, 0.035556, 0.02],
        [None, None, None, 0.25, 0.01104, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None],
        [None, None, None, 0.25, 0.01104, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.04, 0.25, None, None, None],
        [None, None, None, 0.25, 0.01104, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None],
        [None, None, None, 0.25, 0.01104, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.03504, 0.25, 0.02, 0.035556, 0.02],
        [None, None, None, 0.25, 0.01104, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.0268, 0.25, 0.02, 0.035556, 0.02],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.282222, 0.02, None, None, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.04, 0.25, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.02964, 0.25, None, None, None],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, None, None, None, 0.25, 0.03504, 0.25, 0.02, 0.035556, 0.02],
        [0.02, 0.08, 0.02, 0.25, 0.0382, 0.25, 0.02, 0.237778, 0.02, 0.5, 0.625333, 0.5, 0.02, 0.128889, 0.02, 0.25, 0.0268, 0.25, 0.02, 0.035556, 0.02]
        # demais rotas para o Hospital 1
    ]

    # Definição das colunas
    colunas = [
        "EMBARQ1_AMBU", "VIAGEM1_AMBU", "DESEMB1_AMBU", "EMBARQ1_HELI", "VIAGEM1_HELI", "DESEMB1_HELI",
        "EMBARQ2_AMBU", "VIAGEM2_AMBU", "DESEMB2_AMBU", "EMBARQ1_AVIA", "VIAGEM1_AVIA", "DESEMB1_AVIA", "EMBARQ3_AMBU",
        "VIAGEM3_AMBU", "DESEMB3_AMBU", "EMBARQ2_HELI", "VIAGEM2_HELI", "DESEMB2_HELI", "EMBARQ4_HELI", "VIAGEM4_HELI",
        "DESEMB4_HELI"
    ]

    lowest_total_time = float('inf')
    fastest_route = None  # Inicializa a rota mais rápida como None

    # Mapeando os valores das colunas para os meios de transporte
    transportes = {'AMBU': 'Ambulância', 'HELI': 'Helicóptero', 'AVIA': 'Avião'}

    for route in data:
        total_time = sum(value for value in route if value is not None)
        if total_time < lowest_total_time:
            lowest_total_time = total_time
            fastest_route = route

    if fastest_route is not None:  # Verifica se a rota mais rápida foi encontrada

        # Obtendo os trechos usados na rota mais rápida
        trechos_usados = []
        transporte_atual = None
        for i, valor in enumerate(fastest_route):
            if valor is not None:
                nome_coluna = colunas[i]
                partes_coluna = nome_coluna.split('_')
                transporte = transportes[partes_coluna[-1]]
                if transporte != transporte_atual:
                    trechos_usados.append(transporte)
                    transporte_atual = transporte

        print(f'TRANSPORTES USADOS: {" -> ".join(trechos_usados)}')
        print(f'MENOR ROTA: {fastest_route} \nTEMPO TOTAL: {lowest_total_time}')
    else:
        print("Nenhuma rota válida encontrada.")

if __name__ == '__main__':
    main()