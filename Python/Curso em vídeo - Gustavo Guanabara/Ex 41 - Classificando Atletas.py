# ===== DESAFIO 041 =====

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

import datetime
nascimento = int(input("A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.\nDigite o ano de nascimento do atleta: "))
ano_atual = datetime.date.today().year

idade = ano_atual - nascimento

if idade <= 9:
    print("O atleta está na categoria MIRIM.")
elif idade <= 14:
    print("O atleta está na categoria INFANTIL.")
elif idade <= 19:
    print("O atleta está na categoria JÚNIOR.")
elif idade <= 25:
    print("O atleta está na categoria SÊNIOR.")
else:
    print("O atleta está na categoria MASTER.")
