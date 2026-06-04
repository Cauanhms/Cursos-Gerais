# ===== DESAFIO 030 =====

# Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f'O número {num} é PAR.')
elif num % 2 == 1:
    print(f'O número {num} é ÍMPAR.')
elif num == 0:
    print(f"O número é ZERO, ele é considerado PAR.")
else:
    print('Número inválido, tente novamente.')
