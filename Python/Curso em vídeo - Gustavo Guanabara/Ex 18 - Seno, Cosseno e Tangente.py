# ===== DESAFIO 018 =====

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno de {angulo}° é igual a {seno:.2f}.')
print(f'O cosseno de {angulo}° é igual a {cosseno:.2f}.')
print(f'A tangente de {angulo}° é igual a {tangente:.2f}.')
