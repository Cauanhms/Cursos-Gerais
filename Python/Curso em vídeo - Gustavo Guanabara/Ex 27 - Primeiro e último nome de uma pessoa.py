# ===== DESAFIO 027 =====

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: "))
nome_separado = nome.split()
print("\nMuito prazer em te conhecer!")
print(f"Seu primeiro nome é: {nome_separado[0].capitalize}")
print(f'Seu último nome é: {nome_separado[-1].capitalize}')
