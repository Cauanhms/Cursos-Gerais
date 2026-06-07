# ===== DESAFIO 084 =====

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporario = []
principal = []
maior = menor = 0

while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso (Kg): ")))
    
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
            
    principal.append(temporario[:])
    temporario.clear()
    
    resposta = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if resposta == "N":
        break
    
print("==" * 20)
print(f"Ao todo, você cadastrou {len(principal)} pessoas.")

# Mostrando os mais pesados
print(f"O maior peso foi de {maior}Kg. Peso de: ", end="")
for pessoa in principal:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end="")
print()  # Quebra de linha

# Mostrando os mais leves
print(f"O menor peso foi de {menor}Kg. Peso de: ", end="")
for pessoa in principal:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}] ", end="")
print()
