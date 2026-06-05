# ===== DESAFIO 051 =====

# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.

print("==" * 20)
print("10 TERMOS DE UMA P.A")
print("==" * 20)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

décimo = primeiro + (10-1) * razao

for i in range(primeiro, (décimo+1) + razao, razao):
    print(i)
    print(end=" - ")
    
print("\nAcabou!")
