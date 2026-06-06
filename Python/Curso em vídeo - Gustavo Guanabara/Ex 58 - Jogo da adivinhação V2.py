from random import randint
from time import sleep

acerto = False
palpites = 1

print("==" * 20)
print("Jogo da adivinhação V2")
print("==" * 20)

print("Selecione o nível de dificuldade: ")
print("[ 1 ] - Muito Fácil (0 a 3)")
print("[ 2 ] - Fácil (0 a 10)")
print("[ 3 ] - Médio (0 a 50)")
print("[ 4 ] - Difícil (0 a 125)")
print("[ 5 ] - Muito Difícil (0 a 500)")
print("[ 6 ] - Impossível (0 a 1250)")

escolha = int(input("\nSua escolha (1 - 6): "))

while escolha < 1 or escolha > 6:
    escolha = int(input("\033[1;31mINVÁLIDO.\033[m Escolha de 1 a 6: "))

limite = 0
dificuldade = ""

if escolha == 1:
    limite = 3
    dificuldade = "\033[1;32mMuito Fácil\033[m"
elif escolha == 2:
    limite = 10
    dificuldade = "\033[1;32mFácil\033[m"
elif escolha == 3:
    limite = 50
    dificuldade = "\033[1;33mMédio\033[m"
elif escolha == 4:
    limite = 125
    dificuldade = "\033[1;31mDifícil\033[m"
elif escolha == 5:
    limite = 500
    dificuldade = "\033[1;31mMuito Difícil\033[m"
elif escolha == 6:
    limite = 1250
    dificuldade = "\033[1;35mImpossível\033[m"

print(f"\nDificuldade selecionada: {dificuldade}")
computador = randint(0, limite)

print("PENSANDO...")
sleep(1)
jogador = int(input(f"Já fiz minha escolha (0 a {limite}), agora sua vez: "))

while jogador < 0 or jogador > limite:
    jogador = int(input(f"\033[1;31mINVÁLIDO.\033[m Escolha de 0 a {limite}: "))

while not acerto:
    if jogador == computador:
        acerto = True
    else:
        palpites += 1
        if jogador < computador:
            jogador = int(input("Mais, tente novamente: "))
        else:
            jogador = int(input("Menos, tente novamente: "))

print(f"\nVocê escolheu a dificuldade: {dificuldade}.")
print(f"Você precisou de {palpites} palpites para acertar.")