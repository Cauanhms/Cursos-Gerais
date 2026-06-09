def se(condicao, valor_verdadeiro, valor_se_falso):
    if condicao:
        return valor_verdadeiro
    else:
        return valor_se_falso
    
alunos =[
    ("João", 40),
    ("Maria", 60),
    ("Pedro", 94),
    ("Ana", 60),
    ("Carlos", 70),
    ("Beatriz", 90),
    ("Ricardo", 80),
    ("Bruno", 56),
    ("Bruna", 54),
    ("Silas", 51),
    ("Patricia", 36),
    ("Tatiane", 82),
    ("Roseane", 36),
    ("Rebeca", 66),
    ("Carlos", 65),
    ("Marcos", 73),
    ("Adriana", 91),
    ("Adriano", 32),
    
]
print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("=="*22)

for nome, nota in alunos:
    situacao = se(nota >= 70, "Aprovado\t🟢", se(nota>=50, "Recuperação\t🟡", "Reprovado\t🔴"))

    print(f"{nome:^15} {nota:^6} {situacao:^13}")

print("=="*22)

print("Estatísticas:")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    if nota >= 70:
        aprovados += 1

    elif nota >= 50:
        recuperacao += 1

    else:
        reprovados += 1

print(f"\nTotal de alunos: {len(alunos)}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")
