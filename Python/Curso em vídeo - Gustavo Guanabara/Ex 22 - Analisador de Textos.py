# ===== DESAFIO 022 =====

# Cria um programa que leia o nome completo de uma pessoa e mostre:

# * O nome com todas as letras em maiusculas
# * O nome com todas minusculas
# * Quantas letras ao todo (sem conter espaços)
# * Quantas letras tem o primeiro nome

nome = str(input("Nome completo: ")).strip()
print(f"Seu nome com todas as letras maiusculas: {nome.upper()}")
print(f'Seu nome em minusculas: {nome.lower()}')
print(f"Seu nome tem: {len(nome) - nome.count(" ")} caracteres (sem condiderar os espaços)")
dividido = nome.split()
print(f"Caracteres somente do seu primeiro nome: {len(dividido[0])}")
