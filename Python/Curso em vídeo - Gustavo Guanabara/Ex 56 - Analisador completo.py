# ===== DESAFIO 056 =====

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
velhohomem = 0
nomevelho = ""
mulhermenos20 = 0

for pessoa in range(1,5):
    print(f"{'==' * 5} {pessoa}ª pessoa {'==' * 5}")
    nome = str(input("Qual o seu nome: ")).title().strip()
    idade = int(input("Qual a sua idade: "))
    sexo = str(input("Qual o seu gênero (M/F): ")).upper().strip()
    
    while sexo != "M" and sexo != "F":
         sexo = str(input("Inválido. Qual o seu gênero (M/F): ")).upper().strip()
    
    somaidade = somaidade + idade
    
    if pessoa == 1 and sexo in "Mm":
        velhohomem = idade
        nomevelho = nome
        
    if sexo in "Mm" and idade > velhohomem:
        velhohomem = idade
        nomevelho = nome
        
    if sexo in "Ff" and idade < 20:
        mulhermenos20 += 1
    
    mediaidade = somaidade / pessoa
    
print(f"\nA média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {velhohomem} anos e se chama {nomevelho}.")
print(f"Ao todo são {mulhermenos20} mulheres com menos de 20 anos de idade.")
    