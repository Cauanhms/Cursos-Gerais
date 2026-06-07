# ===== DESAFIO 070 =====

# Crie um programa que leia o nome e o preço de vários produtos. O programa deve perguntar se o usuário vai continuar. No final mostre:

# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato.

total = totalmil = contagem = 0
menor = 0
barato = ""

print("-" * 30)
print(f"{'LOJA SUPER BARATÃO':^30}")
print("-" * 30)

while True:
    print(f"\n{'=' * 30}")
    
    produto = str(input("Nome do produto: ")).strip().title()
    preco = float(input("Preço: R$"))
    
    contagem += 1
    total += preco
    
    if preco > 1000:
        totalmil += 1
    
    if contagem == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N]: ")).upper().strip()
    
    if resposta == "N":
        break

print("\n" + "-" * 30)
print(f"O total da compra foi: R${total:.2f}")
print(f"Temos {totalmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi: {barato} que custa R$ {menor:.2f}")
print("-" * 30)