print("========== Carrinho de Compra ==========")
total = 0
carrinho = []

print("")
while True:
    print("==" * 20)
    item = input('Item (ou "sair" para finalizar): ').strip().title()
    if item == "Sair":
        break

    try:
        quantidade = int(input(f"Qual a quantidade de {item} que você deseja: "))
        valor = float(input(f"Qual o valor unitário do item {item}: R$"))
    except ValueError:
        print("Por favor, insira valores numéricos válidos para quantidade e preço.")
        continue

    subtotal_item = quantidade * valor
    total += subtotal_item
    
    carrinho.append(f"{item}: Preço unitário: R${valor:.2f}\nx{quantidade} {item} = R${subtotal_item:.2f}")

subtotal_geral = total

if total > 100:
    total = total * 0.90
    print("\nParabéns! Você ganhou 10% de desconto por comprar acima de R$100!")

print("\n========== Valor da Compra ==========")
for item_carrinho in carrinho:
    print("__" * 20)
    print(item_carrinho)
print("__" * 20)

print(f"\nSubtotal: R${subtotal_geral:.2f}")
print(f"Total à pagar: R${total:.2f}")
