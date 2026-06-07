# ===== DESAFIO 082 =====

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie duas listas extras que vão conter apenas valores pares e os ímpares digitados, respectivamente. Ao final, mostre o conteúdo das 3 listas geradas.

numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input("\nDigite um número: ")))
    resposta = str(input("Quer continuar (S/N): ")).strip().upper()
    
    if resposta == 'N':
        break

for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
                
print("==" * 20)
print(f"A lista completa é: {numeros}")
print(f"A lista de pares: {pares}")
print(f"A lista de ímpares: {impares}")
