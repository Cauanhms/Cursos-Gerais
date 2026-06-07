# ===== DESAFIO 061 =====

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("==" * 15)
print("Gerador de P.A - com while")
print("==" * 15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da P.A: "))
termo = primeiro
contagem = 1

while contagem <= 10:
    if contagem <= 9:
        print(f"{termo} -> ",end="")
        termo = termo + razao
        contagem += 1
    
    else:
        print(f"{termo}.",end="")
        contagem += 1
print("\nFIM")
