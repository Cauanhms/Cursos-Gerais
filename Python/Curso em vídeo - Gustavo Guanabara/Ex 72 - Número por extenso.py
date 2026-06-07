# ===== DESAFIO 072 =====

# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de 0 a 20.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrar como extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

while True:
	numero = int(input('Digite um número entre 0 e 20: '))
	if 0 <= numero <= 20:
		break
	print('Tente novamente.', end =' ')
print(f'Voce digitou o número {cont[numero]}')
