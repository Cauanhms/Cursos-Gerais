# ===== DESAFIO 055 =====

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.

maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input(f"Qual o peso da {pessoa}ª pessoa: "))
    if pessoa == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
            
print(f"\nO maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")
