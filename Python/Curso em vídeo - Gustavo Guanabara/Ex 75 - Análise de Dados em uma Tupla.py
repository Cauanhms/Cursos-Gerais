# ===== DESAFIO 075 =====

# Desenvolva um programa que leia 4 valores pelo teclado guarde-os em uma tupla. No final mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (
    int(input('Digite um número: ')), 
    int(input('Digite outro número: ')), 
    int(input('Digite mais um número: ')), 
    int(input('Digite o último número: '))
)

print(f'\nVocê digitou os valores: {num}')
print("-" * 40)

print(f'O valor 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O valor 3 apareceu primeiro na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

valores_pares = 0
for n in num:
    if n % 2 == 0:
        valores_pares += 1

if valores_pares > 0:
    print('Os valores pares digitados foram: ', end='')
    for n in num:
        if n % 2 == 0:
            print(f'{n} ', end='')
    print()
    
else:
    print("Nenhum valor par foi digitado!")
    
print("-" * 40)
