# ===== DESAFIO 047 =====

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

escolha = int(input("Digite um número para mostrar os pares entre 1 e o número digitado: "))

if escolha < 1:
    print("Número inválido! Tente novamente.")
    exit()

for pares in range(1, escolha + 1):
    if pares % 2 == 0:
        print(pares, end="-")
        
print(f"\n\nEsses são todos os números pares entre 1 e {escolha}.")
