# ===== DESAFIO 015 =====

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quantidade_km = float(input('Quantos Km foram percorridos? '))
quantidade_dias = int(input('Por quantos dias o carro foi alugado? '))
preco_km = quantidade_km * 0.15
preco_dias = quantidade_dias * 60
preco_total = preco_km + preco_dias
print(f'O preço a pagar é de R${preco_total:.2f}.')
