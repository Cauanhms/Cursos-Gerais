# ===== DESAFIO 010 =====

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 5.25
euro = carteira / 5.90
print(f'Com R${carteira:.2f} você pode comprar US${dolar:.2f} ou €{euro:.2f}')
