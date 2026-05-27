# ===== DESAFIO 023 ====

# Faça um programa que leia um número e mostre na tela com cada conjunto de unidade separados

numero = input("Digite um número inteiro de 4 dígitos: ").strip()

while len(numero) != 4 or not numero.isdigit():
    numero = input("Entrada inválida! Digite um número inteiro de 4 dígitos: ").strip()

numero_tipado = int(numero)

unidade = numero_tipado // 1 % 10
dezena = numero_tipado // 10 % 10
centena = numero_tipado // 100 % 10
milhar = numero_tipado // 1000 % 10

print("\nAnalisando o número, ele tem: ")
print(f"Unidades: {unidade}")
print(f"Dezenas: {dezena}")
print(f"Centenas: {centena}")
print(f"Milhares: {milhar}")
