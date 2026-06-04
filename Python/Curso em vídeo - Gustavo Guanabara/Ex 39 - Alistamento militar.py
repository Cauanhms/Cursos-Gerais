# ===== DESAFIO 039 =====

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
if idade < 18:
    print(f"Você tem {idade} anos, ainda vai se alistar ao serviço militar.")
    print(f"Faltam {18 - idade} anos para o alistamento.")
    
elif idade == 18:
    print(f"Você tem {idade} anos, é a hora de se alistar ao serviço militar.")
    
elif idade > 18:
    print(f"Você tem {idade} anos, já passou do tempo do alistamento.")
    print(f"Passaram-se {idade - 18} anos do prazo de alistamento.")
    