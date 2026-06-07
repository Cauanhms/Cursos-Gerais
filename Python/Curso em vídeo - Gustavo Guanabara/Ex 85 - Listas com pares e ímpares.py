# ===== DESAFIO 085 =====

# Cria um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

num = [[ ], [ ]]
valor = 0
for c in range(1,8):
	valor = int(input(f'Digite o {c}° valor: '))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
print('-÷-' * 20)
print(f'Todos os valores: {num}')
print(' ')
num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
