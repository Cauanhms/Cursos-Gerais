# ===== DESAFIO 078 =====

# Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e menor valores digitados e as suas respectivas posições na lista.

listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor na posição {c +1}: ")))
    
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
            
print("==" * 20)
print(f"Você digitou os valores: {listanum}")

print(f"O maior número digitado foi: {maior} nas posições ", end="")
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f"{indice+1}... ", end="")
print()

print(f"O menor número digitado foi: {menor} nas posições ", end="")
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f"{indice+1}... ", end="")
print()
