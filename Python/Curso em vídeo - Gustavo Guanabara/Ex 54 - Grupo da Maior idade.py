# ===== DESAFIO 054 =====

# Crie um programa que leia o ano de nascimento (melhorei a complexidade) de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
mesatual = date.today().month
diaatual= date.today().day

totalmaior = 0
totalmenor = 0

print("==" * 20)
print("Verificador de idade")
print("==" * 20)

for pessoas in range(1,8):
    print(f"\nConsidere a data atual: {diaatual}/{mesatual}/{anoatual}")
    anonascimento = (int(input(f"Em que ano a {pessoas}ª pessoa nasceu: ")))
    
    idade = anoatual - anonascimento
    
    if idade == 18:
        mesnascimento = int(input(f"Em que mês a {pessoas}ª pessoa nasceu: "))
        
        if mesnascimento == mesatual:
            dianascimento = int(input(f"Em que dia a {pessoas}ª pessoa nasceu: "))
            
            if dianascimento < diaatual:
                totalmenor += 1
            elif dianascimento == diaatual:
                totalmaior += 1
                print("Feliz aniversário, 18 aninhos hein!")
            else:
                totalmaior += 1
                
        elif mesnascimento < mesatual:
            totalmenor += 1
        else:
            totalmaior += 1
      
    elif idade > 18:
        totalmaior += 1
        
    else:
        totalmenor += 1
        
print(f"\nNúmero de pessoas que são de menor de idade: {totalmenor}.")
print(f"Número de pessoas que são de maior de idade: {totalmaior}.")
