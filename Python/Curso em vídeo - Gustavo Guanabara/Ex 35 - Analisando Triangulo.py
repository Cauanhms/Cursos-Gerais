# ===== DESAFIO 035 =====

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('==' * 20)
print('Analisador de Triângulos')
print('==' * 20)

reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("As retas acima PODEM FORMAR um triângulo.")
else:
    print("As retas acima NÃO PODEM FORMAR um triângulo.")
     