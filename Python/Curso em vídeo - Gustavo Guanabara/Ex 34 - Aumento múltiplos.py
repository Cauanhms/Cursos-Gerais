# ===== DESAFIO 034 =====

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o salário do funcionário: R$"))
if salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O salário do funcionário era R${salario:.2f} e com o aumento de 10% ele passará a receber R${novo_salario:.2f}.")
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"O salário do funcionário era R${salario:.2f} e com o aumento de 15% ele passará a receber R${novo_salario:.2f}.") 
