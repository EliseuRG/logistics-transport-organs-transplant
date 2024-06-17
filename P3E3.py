class Grafo:

    # Aqui, estamos definindo a classe Grafo. 
    # No método __init__, inicializamos o grafo com o número de vértices (self.V) e uma lista vazia para representar as arestas (self.grafo).
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    # Este método adiciona uma aresta ao grafo. Recebe como parâmetros os vértices de origem (u) e destino (v), e o peso (w) da aresta.
    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    # Este método implementa a operação find (encontrar) do algoritmo de conjuntos disjuntos (union-find). 
    # Ele retorna o representante do conjunto ao qual o vértice i pertence.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Este método implementa a operação union (união) do algoritmo de conjuntos disjuntos (union-find).
    # Ele une os conjuntos que contêm os vértices x e y.
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Este método implementa o algoritmo de Kruskal para encontrar a árvore geradora mínima.
    # Ele ordena as arestas pelo peso, então itera sobre elas, adicionando as arestas à árvore resultante se não formarem um ciclo.
    def kruskal(self):
        resultado = []
        i, e = 0, 0

        # Ordena a lista de arestas self.grafo com base no peso (item[2]) de cada aresta.
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        # Essa ordenação garante que as arestas com os menores pesos sejam as primeiras a
        # serem consideradas na iteração principal do algoritmo.

        parent = []
        rank   = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Percorre as arestas ordenadas.
        # Para cada aresta, ele verifica se a adição da aresta à árvore geradora parcial resultante criaria um ciclo.
        # Se não criar ciclo, a aresta é adicionada à árvore geradora e ao peso total da MST.
        # Como as arestas são consideradas em ordem não decrescente de peso, o algoritmo tende a selecionar as arestas
        # com os menores pesos primeiro, o que contribui para a construção de uma MST com o menor peso total possível.
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.union(parent, rank, x, y)

        return resultado

# Esta é a função principal do programa. Ela cria o grafo com as cidades e suas distâncias, executa o algoritmo de Kruskal e
# imprime as arestas da árvore geradora mínima resultante.
def main():
    cidades = ['L', 'CM', 'NY', 'Pa', 'Pe', 'T']
    grafo = Grafo(len(cidades))

    # Adicionando as arestas conforme a tabela de distâncias
    grafo.add_aresta(0, 3, 214)
    grafo.add_aresta(0, 4, 5074)
    grafo.add_aresta(0, 1, 5558)
    grafo.add_aresta(0, 2, 3469)
    grafo.add_aresta(0, 5, 5959)
    grafo.add_aresta(1, 2, 2090)
    grafo.add_aresta(1, 3, 5725)
    grafo.add_aresta(1, 4, 7753)
    grafo.add_aresta(1, 5, 7035)
    grafo.add_aresta(2, 3, 3636)
    grafo.add_aresta(2, 4, 6844)
    grafo.add_aresta(2, 5, 6757)
    grafo.add_aresta(3, 4, 5120)
    grafo.add_aresta(3, 5, 6053)
    grafo.add_aresta(4, 5, 1307)

    resultado = grafo.kruskal()
    print("Arestas da Árvore Geradora Mínima:")
    for u, v, peso in resultado:
        print(f"{cidades[u]} - {cidades[v]}: {peso}")


if __name__ == "__main__":
    main()


# COMPLEXIDADE

# A complexidade computacional do algoritmo de Kruskal em Python, tanto no pior caso quanto no caso médio, é de O(m log n), onde:

# m representa o número de arestas no grafo.
# n representa o número de vértices no grafo.

# 1. Ordenação das Arestas:
# A ordenação inicial das arestas usando a função sorted leva tempo de O(m log m).
# Como na maioria dos casos, m <= n, a ordenação pode ser considerada como O(m log n).

# 2. Iteraçãoo Principal:
# O loop principal do algoritmo itera sobre as arestas ordenadas, realizando as seguintes operações:
# Verificação de ciclo: A operação find para verificar se a adição da aresta cria um ciclo leva tempo de O(n).
# União de conjuntos: A operação union para unir os conjuntos de vértices conectados pela aresta leva tempo de O(n) amortizado, considerando a otimização de compactação de caminho.
# O número de iterações do loop é m - n + 1, pois a MST contém n - 1 arestas para um grafo com n vértices.
# ultiplicando o tempo por iteração pelo número de iterações, obtemos O(m n - mn + n) = O(mn).

# 3. Complexidade Total:
# Combinando o custo da ordenação e da iteração principal, a complexidade total do algoritmo de Kruskal é O(m log n + mn) = O(mn).
# Como na maioria dos casos, m <= n, a complexidade dominante é O(m log n).