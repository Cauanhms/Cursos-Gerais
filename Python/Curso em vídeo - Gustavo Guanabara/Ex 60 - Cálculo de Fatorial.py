# ===== DESAFIO 060 =====

# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Jeito 1 (com módulo)

from math import factorial

numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = factorial(numero)
print(f"O fatorial de {numero} é {fatorial}.")

# Jeito 2 (com while)

numerov2 = int(input("Digite um número para calcular seu fatorial: "))
index = numero
fatorialv2 = 1

print()