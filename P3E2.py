import time

# Fibonacci Recursivo
def fibonacci_recursivo(n):
    # Base case: Se n for 0 ou 1, retorna n.
    if n < 2:
        return n
    else:
        # Chamadas recursivas para calcular Fibonacci(n - 1) e Fibonacci(n - 2)
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci com Programação Dinâmica
def fibonacci_dinamico(n):
    # Inicializa uma lista com os dois primeiros números de Fibonacci
    fib = [0, 1] + [0] * (n - 1)
    # Preenche a lista com os valores de Fibonacci até o n-ésimo número
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    # Retorna o n-ésimo número de Fibonacci
    return fib[n]

# Testando os algoritmos com n = 10
start = time.time()
print(fibonacci_recursivo(10))
end = time.time()
print("Tempo de execução do Fibonacci Recursivo com n = 10: ", end - start)

start = time.time()
print(fibonacci_dinamico(10))
end = time.time()
print("Tempo de execução do Fibonacci Dinâmico com n = 10: ", end - start)

# Testando os algoritmos com n = 100
start = time.time()
print(fibonacci_dinamico(40))
end = time.time()
print("Tempo de execução do Fibonacci Dinâmico com n = 40: ", end - start)

start = time.time()
print(fibonacci_recursivo(40))
end = time.time()
print("Tempo de execução do Fibonacci Recursivo com n = 40: ", end - start)




# Análise da Complexidade do Algoritmo de Fibonacci Recursivo: 

# O algoritmo recursivo de Fibonacci apresenta uma complexidade exponencial, especificamente O(2^n). 
# Isso ocorre devido à natureza recursiva do algoritmo, onde cada chamada da função F(n) resulta em duas novas chamadas: F(n-1) e F(n-2). 
# Consequentemente, o número de chamadas cresce exponencialmente à medida que n aumenta.

# Uma análise mais detalhada revela que, para n < 2, a função retorna n diretamente, resultando em uma operação constante, ou seja, O(1). 
# No entanto, para n > 2, o algoritmo realiza duas chamadas recursivas. 
# Cada uma dessas chamadas, por sua vez, faz suas próprias chamadas recursivas, criando uma árvore de chamadas recursivas com uma altura de n e aproximadamente 2^n nós, 
# representando cada chamada de função. Portanto, a complexidade de tempo é O(2^n), tornando-se altamente ineficiente para valores grandes de n.

# Análise da Complexidade do Algoritmo de Fibonacci Dinâmico:

# O algoritmo de Fibonacci dinâmico adota uma abordagem "bottom-up", construindo a solução a partir dos casos base até chegar ao caso desejado.
# Esta abordagem é mais eficiente do que a recursão, pois evita recalculos redundantes.
# O algoritmo inicia a construção da tabela armazenando os números de Fibonacci conhecidos (casos base) em um vetor de tamanho n+1.
# Em seguida, preenche iterativamente o vetor para cada índice i de 2 até n, calculando F(i) com base nos valores armazenados em F(i-1) e F(i-2).
# A complexidade de tempo do algoritmo dinâmico é O(n), pois realiza uma única passagem pelo vetor, calculando cada número de Fibonacci uma vez. 
# Da mesma forma, a complexidade de espaço é O(n), pois o algoritmo armazena todos os números até n no vetor.