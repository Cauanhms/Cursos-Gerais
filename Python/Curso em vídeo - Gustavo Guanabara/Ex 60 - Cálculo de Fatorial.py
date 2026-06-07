# ===== DESAFIO 060 =====

# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Jeito 1 (com módulo)
print("===== Com módulos =====")
from math import factorial

numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = factorial(numero)
print(f"O fatorial de {numero} é {fatorial}.")

# Jeito 2 (com while)

print("\n===== Com while =====")
numerov2 = int(input("Digite um número para calcular seu fatorial: "))
index = numerov2 
fatorialv2 = 1

print(f"Calculando {numerov2}! = ", end="")
while index > 0:
    print(f"{index}", end="")
    if index > 1:
        print(" x ", end="")
    else:
        print(" = ", end="")
    
    fatorialv2 = fatorialv2 * index
    index -= 1

print(f"{fatorialv2}")
