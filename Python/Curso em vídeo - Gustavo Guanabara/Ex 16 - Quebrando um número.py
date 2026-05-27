# ===== DESAFIO 016 =====

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
numero = float(input('Digite um número real: '))
print(f'O número digitado foi {numero} e a sua porção inteira é {trunc(numero)}.')
