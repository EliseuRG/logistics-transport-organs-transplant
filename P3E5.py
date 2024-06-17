# A) A estratégia de programação dinâmica:
# Constitui um processo de recursão no qual dois procedimentos recursivos idênticos são computados uma única vez.

def fibonacci_dinamico(n, memo={}):
  """
  Calcula o n-ésimo termo da Sequência de Fibonacci utilizando Programação Dinâmica.

  Argumentos:
    n (int): Posição do termo desejado na sequência.
    memo (dict): Dicionário para armazenar os valores já calculados.

  Retorno:
    int: Valor do n-ésimo termo da Sequência de Fibonacci.
  """

  if n in memo:
    return memo[n]

  if n == 0:
    valor = 0
  elif n == 1:
    valor = 1
  else:
    valor = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)

  memo[n] = valor
  return valor
