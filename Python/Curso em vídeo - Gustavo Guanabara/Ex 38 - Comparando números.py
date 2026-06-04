# ===== DESAFIO 038 =====

# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela numa mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    print(f"O primeiro valor é maior: {numero1} > {numero2}.")
elif numero2 > numero1:
    print(f"O segundo valor é maior: {numero2} > {numero1}.")
elif numero1 == numero2:
    print(f"Não existe valor maior, os dois são iguais: {numero1} = {numero2}.")
else:
    print("Número inválido, tente novamente.") 
