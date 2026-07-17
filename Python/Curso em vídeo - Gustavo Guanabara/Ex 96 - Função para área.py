# ===== DESAFIO 096 =====

# Crie um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e  mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área do terreno de {largura:.2f}m x {comprimento:.2f}m é de {area:.2f}m².")
    
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
area(largura, comprimento)
