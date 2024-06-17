# A primeira versão implementa o algoritmo de Dijkstra para encontrar a rota mais curta entre um ponto de partida e todos os outros pontos em um grafo. 
# No entanto, para torná-lo mais robusto e alinhado com o problema do caixeiro viajante, foi adicionado uma função para encontrar a rota completa mais curta
# que visita todos os pontos uma vez e retorna ao ponto de partida:

import heapq

def calcular_rota_mais_curta(graph, start):
    distances = {node: float('infinity') for node in graph}
    previous_nodes = {node: None for node in graph}
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
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

def calcular_rota_completa(graph, start):
    distances, previous_nodes = calcular_rota_mais_curta(graph, start)
    nodes = list(graph.keys())
    nodes.remove(start)
    route = [start]

    while nodes:
        next_node = min(nodes, key=lambda node: distances[node])
        nodes.remove(next_node)
        route.append(next_node)

    route.append(start)
    return route

# Exemplo de uso:
graph = {
    'Depósito': {'Ponto1': 2, 'Ponto2': 5, 'Ponto3': 10},
    'Ponto1': {'Depósito': 2, 'Ponto2': 3, 'Ponto3': 2},
    'Ponto2': {'Depósito': 5, 'Ponto1': 3, 'Ponto3': 1},
    'Ponto3': {'Depósito': 10, 'Ponto1': 2, 'Ponto2': 1}
}
print(calcular_rota_completa(graph, 'Depósito'))

#  A rota é determinada escolhendo o próximo ponto a ser o ponto não visitado mais próximo do ponto de partida atual.

#----------------------| COMPLEXIDADE |----------------------#
# A complexidade do tempo de execução do algoritmo de Dijkstra é O((V+E) log V), onde V é o número de vértices (nós) no gráfico e E é o número de arestas.

# A função calcular_rota_completa tem uma complexidade de tempo de execução de O(V^2), pois para cada nó, ele procura o nó não visitado mais próximo.

# Portanto, a complexidade total do tempo de execução do código é dominada pela função calcular_rota_completa e é O(V^2).

# No entanto, se considerarmos a complexidade do espaço, o algoritmo de Dijkstra tem uma complexidade de espaço de O(V), pois mantém um registro das distâncias e nós anteriores para cada nó no gráfico.

# A função calcular_rota_completa também tem uma complexidade de espaço de O(V), pois mantém uma lista dos nós a serem visitados e a rota atual.

# Portanto, a complexidade total do espaço do código é O(V).


#----------------------| PROJETO DE ALGORITMO |----------------------#

# O código que você forneceu implementa o algoritmo de Dijkstra para encontrar a rota mais curta entre um ponto de partida e todos os outros pontos em um grafo. Ele também implementa uma função para encontrar a rota completa mais curta que visita todos os pontos uma vez e retorna ao ponto de partida.

# Aqui está uma explicação passo a passo do algoritmo:

# A função calcular_rota_mais_curta começa inicializando as distâncias de todos os nós para infinito, exceto o nó de partida, cuja distância é definida como 0. Ela também inicializa uma fila de prioridade com o nó de partida.

# Em seguida, entra em um loop onde extrai o nó com a menor distância da fila de prioridade.

# Se a distância atual do nó extraído for maior do que a distância registrada para esse nó, ele continua para a próxima iteração do loop. Isso ocorre porque uma distância menor foi encontrada para esse nó desde que foi adicionado à fila de prioridade.

# Caso contrário, ele percorre todos os vizinhos do nó extraído. Para cada vizinho, ele calcula a distância para o vizinho através do nó extraído.

# Se a distância calculada for menor do que a distância registrada para o vizinho, ele atualiza a distância registrada e adiciona o vizinho à fila de prioridade.

# A função calcular_rota_completa usa a função calcular_rota_mais_curta para obter as distâncias mais curtas para todos os nós a partir do nó de partida. Em seguida, ele constrói a rota completa mais curta, começando pelo nó de partida e sempre indo para o nó não visitado mais próximo, até que todos os nós tenham sido visitados. Finalmente, ele retorna ao nó de partida.

# Espero que isso ajude a entender como o algoritmo foi implementado no seu código.