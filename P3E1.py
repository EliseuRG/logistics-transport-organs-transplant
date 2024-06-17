# Pontifícia Universidade Católica de Goiás
# Escola Politécnica - Departamento de Computação
# Projeto e Análise de Algoritmos
# Prof. Phd. Marco Antônio
# Aluno: Eliseu Rodrigues Guimarães

# Path: Questão 1 - Divisão e Conquista
# Compare o tempo de execução dos algoritmos de ordenação por seleção e mergesort. Utilize vetores de tamanho 10 e 100.

# MERGE SORT.....: A divisão ocorre em cada chamada recursiva do mergesort linha (39 até 45), enquanto a conquista ocorre na mesclagem dos vetores ordenados.
# SELECTION SORT.: A seleção ocorre na escolha do menor elemento não ordenado, enquanto a conquista ocorre na troca desse elemento com o primeiro não ordenado.


# Importa as bibliotecas necessárias
import time
import random
import matplotlib.pyplot as plt

# Função de ordenação por seleção
def selection_sort(A):

    # Percorre todos os elementos do vetor
    for i in range(len(A)):

        # Assume que o elemento atual é o mínimo
        min_idx = i

        # Percorre os elementos à direita do atual
        for j in range(i+1, len(A)):

            # Se o elemento atual é menor que o mínimo, atualiza o mínimo
            if A[j] < A[min_idx]:
                min_idx = j

        # Troca o elemento mínimo com o primeiro elemento não ordenado
        A[i], A[min_idx] = A[min_idx], A[i]

    return A

# ---------------------------------------------------------------
# Divisão: O algoritmo divide o array de entrada em duas metades. Isso é feito em tempo constante, então a complexidade de tempo para essa etapa é O(1).
# Função de ordenação mergesort
def merge_sort(A):
    # Se o vetor tem mais de um elemento
    if len(A) > 1:
        
        # Divide o vetor no meio
        mid = len(A) // 2

        # Ordena a metade esquerda
        left = merge_sort(A[:mid])

        # Ordena a metade direita
        right = merge_sort(A[mid:])

        # Mescla as duas metades ordenadas
        A = merge(left, right)
        #plot_vector(A)  # Plota o vetor após cada mesclagem
    return A



# Função de mesclagem
def merge(left, right):

    # Inicializa o vetor resultado
    result = []
    i = j = 0

    # Enquanto há elementos em ambos os vetores
    while i < len(left) and j < len(right):

        # Adiciona o menor elemento ao vetor resultado e avança o índice correspondente
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adiciona os elementos restantes do vetor esquerdo, se houver
    while i < len(left):
        result.append(left[i])
        i += 1

    # Adiciona os elementos restantes do vetor direito, se houver
    while j < len(right):
        result.append(right[j])
        j += 1

    # Retorna o vetor resultado
    return result

# ---------------------------------------------------------------
# Função para plotar um vetor
def plot_vector(A):
    plt.clf()  # Limpa a figura atual
    plt.bar(range(len(A)), A)  # Cria um gráfico de barras com os valores do vetor
    plt.pause(0.01)  # Pausa por 0.01 segundos

# ---------------------------------------------------------------
# Testa as funções de ordenação com vetores de tamanho 10 e 100
for n in [10, 100]:

    # Gera um vetor aleatório
    A = [random.randint(1, 1000) for _ in range(n)]

    # Mede o tempo de execução da ordenação por seleção
    start_selection = time.time()
    selection_sort(A)
    end_selection = time.time()

    # Gera um novo vetor aleatório
    A = [random.randint(1, 1000) for _ in range(n)]

     # Permite a atualização do gráfico em tempo real
    #plt.show(block=False)

    # Mede o tempo de execução do mergesort
    start_merge = time.time()
    merge_sort(A)
    end_merge = time.time()

    # Garante que o último gráfico seja exibido corretamente
    #plt.show()

    # Imprime os resultados
    print("------------------| COMPARAÇÃO |------------------")
    print("TAMANHO DO VETOR: ", n)
    print(f"SELECTION SORT .: Tempo {format(end_selection - start_selection, '.15f')}")
    print(f"MERGE SORT .....: Tempo {format(end_merge - start_merge, '.15f')}")
    print("-------------------------------------------------")

    # MERGE SORT
    # Portanto, a recorrência para o tempo de execução do Merge Sort é T(n) = 2T(n/2) + O(n).
    # De acordo com o Teorema Mestre, isso resolve para uma complexidade de tempo de O(n log n).

    # SELECTION SORT
    # Por outro lado, o algoritmo Selection Sort não é recursivo e, portanto, o Teorema Mestre não se aplica a ele.
    # A complexidade de tempo do Selection Sort é O(n^2) para todos os casos, pois ele sempre itera sobre todos os
    # elementos do array para cada elemento do array.