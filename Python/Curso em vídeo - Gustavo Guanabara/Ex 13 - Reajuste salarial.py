# ===== DESAFIO 013 =====

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'O salário anterior era R${salario:.2f}. Com 15% de aumento é R${novo_salario:.2f}.')
