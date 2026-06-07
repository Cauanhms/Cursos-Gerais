# ===== DESAFIO 071 =====

# Cria um programa que simule um caixa eletrônico. No início pergunte ao usuário qualquer valor que ele quer sacar. E o programa vai informar quantas cédulas cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de 50 a 1 real.

print("=="*20)
print("Bank2You")
print("=="*20)

valor = int(input("Que valor você quer sacar: R$"))
total = valor
cedula = 50
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f"Total de {totalcedula} cédulas de R${cedula}")
        
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
            
        elif cedula == 10:
            cedula = 1
        
        totalcedula = 0
        if total == 0:
            break
        
print("==" * 20)
print("Volte sempre ao Bank2You! Tenha um ótimo dia!")
