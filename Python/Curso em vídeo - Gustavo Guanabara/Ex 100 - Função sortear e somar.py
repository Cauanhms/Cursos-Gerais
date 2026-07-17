# ===== DESAFIO 100 =====

# Faça um programa que tenha uma lista chamada números a duas Funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar e soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print("─" * 50)
    print("Sorteando 5 valores para a lista: ", end="", flush=True)
    for i in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(f"{numero} ", end="", flush=True)
        sleep(0.3)
    print("─ PRONTO!")

def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f"Somando os valores pares de {lista}, temos o total de: {soma}")
    print("─" * 50)

# Programa Principal
números = list()
sorteia(números)
somaPar(números)