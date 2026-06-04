# ===== DESAFIO 043 =====

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input("Digite o peso da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em metros): "))
imc = peso / (altura ** 2)

print(f"O IMC da pessoa é: {imc:.2f}")

if imc < 18.5:
    print(f"Peso da pessoa: {peso}kg")
    print(f"Altura da pessoa: {altura}m")
    print("Status: Abaixo do Peso")
    
elif 18.5 <= imc < 25:
    print(f"Peso da pessoa: {peso}kg")
    print(f"Altura da pessoa: {altura}m")
    print("Status: Peso Ideal")
    
elif 25 <= imc < 30:
    print(f"Peso da pessoa: {peso}kg")
    print(f"Altura da pessoa: {altura}m")
    print("Status: Sobrepeso")
    
elif 30 <= imc < 40:
    print(f"Peso da pessoa: {peso}kg")
    print(f"Altura da pessoa: {altura}m")
    print("Status: Obesidade")
    
else:
    print(f"Peso da pessoa: {peso}kg")
    print(f"Altura da pessoa: {altura}m")
    print("Status: Obesidade Mórbida")
