# ===== DESAFIO 049 =====

# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("==" * 20)
print("Tabuada - parte 2")
print("==" * 20)

numero = int(input("Digite um número inteiro para ver sua tabuada: "))

for multiplicador in range(1,11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    