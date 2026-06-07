# ===== DESAFIO 087 =====

# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maior = 0

# 1. Entrada de dados na Matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        # Corrigido: Removido o '=' extra
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha+1}] [{coluna+1}]: "))
        
print("==" * 20)

# 2. Mostrando a matriz na tela e calculando a soma dos pares
for linha in range(0, 3):
    for coluna in range(0, 3):  # Corrigido: Adicionado o loop das colunas que faltava
        print(f"{matriz[linha][coluna]:^10}", end="")
        
        # A) Soma de todos os valores pares
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
    
print("==" * 20)

# Exibição do Resultado A
print(f"A soma dos valores pares é {somapar}.")

# B) Cálculo e exibição da soma dos valores da terceira coluna
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f"A soma dos valores da 3ª coluna é {somacoluna}.")

# C) Cálculo e exibição do maior valor da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}.")