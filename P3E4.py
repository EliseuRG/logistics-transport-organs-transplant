# A) A estratégia de divisão e conquista:
# Opera decompondo um problema em subproblemas independentes, resolvendo-os e combinando as soluções
# obtidas em uma solução para o problema original. Isso estabelece um processo recursivo de decomposições e recombinações.

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        # Chamada recursiva para ordenar as sublistas
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Mescla as sublistas ordenadas
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes de esquerda, se houver
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes de direita, se houver
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# Exemplo de uso
lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)
merge_sort(lista)
print("Lista ordenada:", lista)

# Divisão ...: O intervalo de busca inicial é dividido em dois subintervalos.
# Verificação: O elemento procurado é comparado com o elemento no meio do intervalo.
# Recursão ..: Se o elemento procurado for igual ao elemento do meio, a busca termina e a posição do elemento é retornada. Se o elemento procurado for menor que o elemento do meio, a busca é realizada no subintervalo à esquerda. Se o elemento procurado for maior que o elemento do meio, a busca é realizada no subintervalo à direita.
# Repetição .: As etapas 1 a 3 são repetidas até que o elemento seja encontrado ou que o intervalo de busca se torne vazio, indicando que o elemento não está presente na lista.

# COMPLEXIDADE

# Como o número de chamadas recursivas é (log n) e o custo por chamada é constante, a complexidade temporal total da busca binária é O(log n).
# Essa complexidade logarítmica torna a busca binária um algoritmo extremamente eficiente para encontrar elementos em listas grandes,
# pois o tempo de busca cresce muito mais lentamente do que o tamanho da lista.