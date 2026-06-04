# ===== DESAFIO 045 =====

# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print("==" * 20)
print("Vamos jogar Jokenpô!")
print("==" * 20)

jogadas = ("Pedra", "Papel", "Tesoura")

print("Ok, vou pensar na minha jogada...")
sleep(2)
computador = randint(0, 2)

print("Pronto! Agora é a sua vez de escolher:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

jogador = int(input("Sua escolha (0-2): "))
if jogador < 0 or jogador > 2:
    print("Jogada inválida! Tente novamente.")
    exit()

print("\nJO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ!")
print(f"Computador jogou: {jogadas[computador]}")
print(f"Jogador jogou: {jogadas[jogador]}") 

if computador == jogador:
    print("Empate!")
    
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    print("Eu venci!")
    
else:
    print("Parabéns, você venceu!")    