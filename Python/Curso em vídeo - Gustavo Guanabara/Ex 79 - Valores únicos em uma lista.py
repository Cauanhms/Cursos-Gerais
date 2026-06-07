# ===== DESAFIO 079 =====

# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro. Ele não será adicionado. No final, serão, exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()

while True:
    numero = int(input("\nDigite um valor: "))
    
    if numero not in numeros:
        numeros.append(numero)
        print(f"Número computado!")
        
    else:
        print("Valor duplicado. Tente outro valor.")
    
    resposta = str(input("Quer continuar (S/N): ")).strip()
    if resposta in "nN":
        break
    
print("==" * 20)
print(F"Você digitou os valores nessa ordem: {numeros}")
numeros.sort()
print(f"\nAgora vou mostrar em ordem númerica: {numeros}")
