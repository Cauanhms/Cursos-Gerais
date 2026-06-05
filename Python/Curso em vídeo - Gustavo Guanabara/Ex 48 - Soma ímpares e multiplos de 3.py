# ===== DESAFIO 046 =====

# Crie um programa que mostre na tela a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 e 500.

contador = 0
soma = 0

for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        contador += 1
        soma += numero

print(f"A soma dos {contador} números ímpares que são múltiplos de 3 no intervalo entre 1 e 500 é: {soma}.")
