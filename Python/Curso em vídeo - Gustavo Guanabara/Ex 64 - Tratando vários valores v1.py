# ===== DESAFIO 064 =====

# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada. No final mostre quantos números foram digitados e a soma deles (menos o 999)

numero = contagem = soma = 0

numero = int(input("Digite um número (999 para parar): "))

while numero != 999:
    soma = soma + numero
    contagem += 1
    numero = int(input("Digite um número (999 para parar): "))
    
print(f"Você digitou {contagem} números e a soma de todos eles foi: {soma}.")
