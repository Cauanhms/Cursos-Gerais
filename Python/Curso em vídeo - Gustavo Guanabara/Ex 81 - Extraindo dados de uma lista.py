# ===== DESAFIO 081 =====

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e se está ou não na lista.

valores = []

while True:

    valores.append(int(input("\nDigite um valor: ")))
    
    resposta = str(input("Quer continuar (S/N): ")).upper().strip()
    
    if resposta == 'N':
        break
    
print("==" * 20)
    
print(f"Você digitou {len(valores)} elementos.")

valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}")

if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não se encontra na lista...")
    