# ===== DESAFIO 057 =====

# Faça um programa que leia o sexo de uma pessoa, mas só pode aceitar os valores "M" ou "F" caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo (M/F): ")).strip().upper()

while sexo != "M" and sexo != "F":
    sexo = str(input("Inválido. Informe um sexo válido (M/F): ")).upper().strip()
    
if sexo == "M":
    print("Sexo masculino, registrado com sucesso!")
    
elif sexo == "F":
    print("Sexo feminino, registrado com sucesso!")
    