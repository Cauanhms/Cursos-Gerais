# ===== DESAFIO 024 =====

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome: "Santo" mesmo com erro de digitação do usuário.

cidade = str(input('Qual cidade você nasceu: ')).strip().title()

print('\nTem a palavra "Santo" no primeiro nome da cidade:')
print(cidade[:5] == 'Santo')

print('\nTem a palavra "Santo" em qualquer parte do nome da cidade:')
print('Santo' in cidade)
