# ===== DESAFIO 044 =====

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

carrinho = float(input("Digite o valor total do carrinho: R$"))
print("Escolha a forma de pagamento:")
print("==" * 20)
print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")

opcao = int(input("Digite a opção de pagamento (1, 2, 3 ou 4): "))

if opcao == 1:
    valor_final = carrinho * 0.90
    print(f"Valor a ser pago: R${valor_final:.2f} (10% de desconto)")
    
elif opcao == 2:
    valor_final = carrinho * 0.95
    print(f"Valor a ser pago: R${valor_final:.2f} (5% de desconto)")
    
elif opcao == 3:
    valor_final = carrinho
    print(f"Valor a ser pago: R${valor_final:.2f} (preço normal)")
    
elif opcao == 4:
    parcelas = int(input("Digite o número de parcelas (3 ou mais): "))
    if parcelas >= 3:
        valor_final = carrinho * 1.20
        valor_parcela = valor_final / parcelas
        print(f"Valor a ser pago: R${valor_final:.2f} (20% de juros)")
        print(f"Valor de cada parcela: R${valor_parcela:.2f} em {parcelas}x")
    else:
        print("Número de parcelas inválido. Tente novamente.")
