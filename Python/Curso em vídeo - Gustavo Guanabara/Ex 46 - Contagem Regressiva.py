# ===== DESAFIO 046 =====

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from datetime import date

print("==" * 20)
print("Contagem Regressiva para o Ano Novo!")
print("==" * 20)

anoatual = date.today().year
anoquevem = anoatual + 1

for anonovo in range(10, 0, -1):
    print(anonovo)
    sleep(1)
print(f"Feliz Ano Novo!!! Vem {anoquevem}!!!")
