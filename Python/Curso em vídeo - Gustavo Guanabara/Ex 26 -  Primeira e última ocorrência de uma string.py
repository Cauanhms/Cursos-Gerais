# ===== DESAFIO 026 =====

# Faça um programa que leia uma frase pelo teclado e mostre:

# * Quantas vezes aparece a letra "A"
# * Em que posição ela aparece a primeira, e a última vez.

frase = str(input("Digite uma frase: ")).strip().upper()

print(f'\nA letra "A" aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição(caracter) {frase.find("A")} na frase.')
print(f'A última letra A apareceu na posição(caracter) {frase.rfind("A")} na frase.')
print("OBS: ele está considerando os espaços")
