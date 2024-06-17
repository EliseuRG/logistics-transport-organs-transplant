#Vamos considerar um problema de otimização de rotas para um serviço de entrega. O objetivo é encontrar a rota mais curta que um veículo de entrega deve seguir para visitar um conjunto de locais uma única vez e depois retornar ao local de origem. Este é um exemplo do problema do caixeiro viajante, que é um problema clássico de otimização em grafos. Podemos usar o algoritmo de Dijkstra para resolver este problema.

#Aqui está um exemplo de como foi implementado isso em Python:

import heapq

def calcular_rota_mais_curta(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Exemplo de uso:
graph = {
    'Depósito': {'Ponto1'  : 2,  'Ponto2': 5, 'Ponto3': 10},
    'Ponto1'  : {'Depósito': 2,  'Ponto2': 3, 'Ponto3':  2},
    'Ponto2'  : {'Depósito': 5,  'Ponto1': 3, 'Ponto3':  1},
    'Ponto3'  : {'Depósito': 10, 'Ponto1': 2, 'Ponto2':  1}
}
print(calcular_rota_mais_curta(graph, 'Depósito'))