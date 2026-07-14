# ===== DESAFIO 090 =====

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 

aluno = {}
aluno['nome'] = str(input("Nome do aluno: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
    
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
    
print("==" * 20)
for chave, valor in aluno.items():
    print(f"- {chave.title()}: {valor}")
    