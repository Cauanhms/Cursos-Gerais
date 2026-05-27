# ===== DESAFIO 028 =====

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir que foi o número escolhido pelo computador o programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

print("--"*40)
print("Vamos fazer um joguinho? Escolhe um número de 0 a 5 para eu tentar adivinhar!")
print("--"*40)

computador = random.randint(1,5)
time.sleep(1)

jogador = int(input("Pensei no meu número!\nAgora é sua vez: "))


while jogador < 1 or jogador > 5:
    jogador = int(input("Coloque um número válido para jogarmos: "))
    
print("PROCESSANDO OS DADOS...")
time.sleep(2)


if computador == jogador:
    print(f"Parabéns, você conseguiu me vencer, eu pensei o número {computador} e você também pensou no número {jogador}.")
    
else:
    print(f"GANHEI DE VOCÊ!!! Eu pensei no número {computador} e você pensou no número {jogador}. Tente numa próxima.")
