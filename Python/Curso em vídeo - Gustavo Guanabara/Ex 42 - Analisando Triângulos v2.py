# ===== DESAFIO 42 =====

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print("==" * 20)
print("Analisando Triângulos - parte 2")
print("==" * 20)

reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print("As retas acima PODEM FORMAR um triângulo ", end="")
    
    if reta1 == reta2 == reta3:
        print("EQUILÁTERO.")
    elif reta1 != reta2 != reta3 != reta1:
        print("ESCALENO.")
    else:
        print("ISÓSCELES.")
    
else:
    print("As retas acima NÃO PODEM FORMAR um triângulo. Tente novamente.")
