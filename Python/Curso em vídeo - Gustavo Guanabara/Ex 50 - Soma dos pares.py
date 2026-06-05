# ===== DESAFIO 050 =====

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que foram pares. Se o valor digitado for ímpar. Desconsidere-o.

soma = 0 
contador = 0

for valores in range(1, 7):
    numero = int(input(f"Digite o {valores}º número: "))

    if numero % 2 == 1:
        soma = soma + numero
        contador += 1
        
print(f"Você informou {contador} números ímpares. A soma deles deu: {soma}")
