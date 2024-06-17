# Linha de valores com Nones
linha = [0.02, 0.30222, 0.02, None, None, None, 0.5, 0.625333, 0.5, None, None, 0.25, 0.04, 0.25, None, None, None, None, None, None]

# Somar os valores ignorando os Nones
soma = sum(valor for valor in linha if valor is not None)

print("Soma: ", soma)
