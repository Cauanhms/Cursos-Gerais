# ===== DESAFIO 098 =====

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# A) de 1 até 10, de 1 em 1
# B) de 10 até 0, de 2 em 2
# C) uma contagem personalizada

from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        
    elif passo < 0 and inicio < fim:
        passo =- passo
    
    print("")    
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:") 
    
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
            
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ", flush=True)
            sleep(0.5) 

contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input("\nDigite o início da contagem: ")), int(input("Digite o fim da contagem: ")), int(input("Digite o passo da contagem: ")))
