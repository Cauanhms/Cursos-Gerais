# ===== DESAFIO 063 =====

# Escreva um programa que leia um número inteiro qualquer e mostre na tela os primeiros X elementos de uma sequência de Fibonacci.

print('--' * 25)
print('Sequencia de Fibonacci')
print('--' * 25)
n = int(input('Quantos termos voce quer mostar? '))
t1 = 0
t2 = 1
print('~~' * 25)

print(f'{t1} -> {t2}', end=' ')
cont = 3

while cont <= n:
	t3 = t1 + t2
	print(f'-> {t3}', end=' ')
	t1 = t2
	t2 = t3
	cont = cont + 1
print('-> FIM')
