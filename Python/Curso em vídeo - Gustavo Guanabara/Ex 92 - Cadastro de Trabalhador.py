# ===== DESAFIO 092 =====

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantoa anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


from datetime import datetime

dados = {}
dados['nome'] = str(input("Nome: "))

nascimento = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nascimento

dados['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))

if dados['ctps']  != 0:
    dados['ano contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: "))
    dados['aposentadoria'] = dados['idade'] + (dados['ano contratacao'] + 35 - dados['idade'] - nascimento)
    
    print('==' * 20)
    for chave, valor in dados.items():
        print(f"{chave.title()}: {valor}")
