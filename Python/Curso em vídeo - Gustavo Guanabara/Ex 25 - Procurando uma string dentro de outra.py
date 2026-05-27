# ===== DESAFIO 025 =====

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" em qualquer parte de seu nome.

nome = str(input("Qual seu nome completo: "))
print(f'Você tem "Silva" no nome: {"Silva" in nome.title()}')
