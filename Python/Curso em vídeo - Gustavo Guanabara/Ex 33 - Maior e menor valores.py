# ===== DESAFIO 033 =====

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1  = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    maior = numero1

    if numero2 < numero3:
        menor = numero2
    else:
        menor = numero3

elif numero2 > numero1 and numero2 > numero3:
    maior = numero2

    if numero1 < numero3:
        menor = numero1
    else:
        menor = numero3
        
elif numero3 > numero1 and numero3 > numero2:
    maior = numero3

    if numero1 < numero2:
        menor = numero1
    else:
        menor = numero2

print(f"O maior número é {maior} e o menor número é {menor}.")
