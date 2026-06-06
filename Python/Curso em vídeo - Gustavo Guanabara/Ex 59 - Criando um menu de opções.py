# ===== DESAFIO 059 ===== 

# Crie um programa que leia 2 valores e mostre um menu como este:
	
	# [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa.
	
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1= int(input('Primeiro valor: ' ))
n2 = int(input('Segundo valor: '))

opção = 0
while opção != 5:
	print('-÷-' * 25)
	print('''        [ 1 ] Somar
	[ 2 ] Multiplicar
	[ 3 ] Maior
	[ 4 ] Novos Números 
	[ 5 ] Sair do Programa''')
	print('-÷-' * 25)
	opção = int(input('Qual é a sua opção? '))
	if opção == 1:
		soma = n1 +  2
		print(f'A soma entre {n1} e {n2} é {soma}')

	elif opção == 2:
		produto = n1 * n2
		print(f'A multiplicação de {n1} x {n2} é {produto}.')
		
	elif opção == 3:
		if n1 > n2:
			maior = n1
			print(f'Entre {n1} e {n2} o maior valor é {maior}')
		elif n2 > n1:
			maior = n2
			print(f'Entre {n1} e {n2} o maior valor é {maior}')
		else:
			print('Os dois valores são iguais.')
		
	elif opção == 4:
		print('Informe os números novamente: ')
		n1 = int(input('Primeiro valor: '))
		n2 = int(input('Segundo valor: '))
		
	elif opção == 5:
		print('Finalizando...')
		
	else:
		print('Opção inválida. Tente novamente.')
	sleep(1.5)
print('Fim do programa! Volte sempre!')
