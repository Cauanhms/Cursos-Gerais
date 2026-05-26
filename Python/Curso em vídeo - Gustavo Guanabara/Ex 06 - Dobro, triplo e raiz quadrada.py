# ===== DESAFIO 006 =====

# Faça um programa que leia um número inteiro e mostre na tela o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número inteiro: '))
print(f'O número digitado foi {numero}.')
print(f'O dobro de {numero} é {numero * 2}.')
print(f'O triplo de {numero} é {numero * 3}.')
print(f'A raiz quadrada de {numero} é {numero ** (1/2):.2f}.')
