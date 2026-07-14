from random import randint
from time import sleep

lista = list()
jogos = []
print("==" * 20)
print("      JOGO DA MEGA SENA      ")
print("==" * 20)

quantidade = int(input("Quantos jogos você quer que eu sorteie?\nQuantidade: "))
total = 1

while total <= quantidade:
    contador = 0
    
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
            
        if contador >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
        
print("==" * 5, f"   SORTEANDO {quantidade} JOGOS   ", "==" * 5)
for indice, linha in enumerate(jogos):
    print(f"Jogo {indice + 1}: {linha}")
    sleep(1)
print("")
print("Boa sorte!!")
