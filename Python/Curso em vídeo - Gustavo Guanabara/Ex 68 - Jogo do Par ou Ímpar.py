from random import randint

print("==" * 20)
print("JOGO: PAR OU ÍMPAR")
print("==" * 20)

vitoria = 0

while True:
    jogador = int(input("\nDiga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou ímpar (P/I): ")).strip().upper()
    
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}")
    
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
            
    print("\nComputador: Vamos jogar novamente! Eu vou vencer agora!")

print(f"\nGAME OVER! Você venceu {vitoria} vezes.")
