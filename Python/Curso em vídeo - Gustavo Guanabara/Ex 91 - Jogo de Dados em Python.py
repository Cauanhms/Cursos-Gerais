# ===== DESAFIO 091 =====

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
        }

ranking = []

print("==" * 20)
print("Valores sorteados:")
print("")

for jogador, valor in jogo.items():
    print(f"{jogador} tirou {valor} no dado.")
    sleep(1)
    
    ranking.append((jogador, valor))
    
ranking.sort(key=itemgetter(1), reverse=True)

print("==" * 20)
print("Ranking dos jogadores:")
print("")

for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{i}º lugar: {jogador} com {valor} pontos.")
    sleep(1)
    