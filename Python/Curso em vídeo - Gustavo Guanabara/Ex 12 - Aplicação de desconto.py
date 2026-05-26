# ===== DESAFIO 012 =====

# Faça um programa que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

produto = str(input('Digite o nome do produto que vai ter desconto: '))
preco = float(input(f'Digite o preço do {produto}: R$'))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'O preço anterior do {produto} era R${preco:.2f}. Com 5% de desconto é R${novo_preco:.2f}.')
