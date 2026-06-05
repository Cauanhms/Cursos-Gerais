# ===== DESAFIO 053 =====

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. Desconsidere os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = join(palavras)
inverso = junto[::-1]

