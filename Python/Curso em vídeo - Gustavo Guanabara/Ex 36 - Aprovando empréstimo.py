# ===== DESAFIO 036 =====

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual é o valor da casa: R$"))
salario = float(input("Qual é o salário do comprador: R$"))
anos = int(input("Em quantos anos vai ser o financiamento: "))
prestacao = casa / (anos * 12)
minimo = salario * 0.30

print(f"O valor da casa é de R${casa:.2f}. O salário do comprador é de R${salario:.2f}. O financiamento será pago em {anos} anos. O valor da prestação mensal é de R${prestacao:.2f}. O valor máximo permitido para a prestação é de R${minimo:.2f}.")

print(f"O valor da prestação mensal é de R${prestacao:.2f}. O valor máximo permitido para a prestação é de R${minimo:.2f}.")

if prestacao <= minimo:
    print(f"O valor da prestação mensal é de R${prestacao:.2f}. O empréstimo foi APROVADO.")
else:
    print(f"O valor da prestação mensal é de R${prestacao:.2f}. O empréstimo foi NEGADO.")
    