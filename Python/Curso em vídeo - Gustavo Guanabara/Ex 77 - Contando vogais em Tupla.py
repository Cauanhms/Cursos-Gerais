# ===== DESAFIO 077 =====

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar', 'praticar', 'dedicar', 'futuro', 'academia', 'enem', 'passar', 'foco')

for palavras in palavras:
	print(f'\nNa palavra {palavras.upper()} temos:', end=' ')
	for letra in palavras:
		if letra.lower() in 'aeiou':
			print(letra, end=' ')
   