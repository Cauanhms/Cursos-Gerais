pessoas = []
soma_idade = 0

while True:
    nome = input("Nome: ")
    
    # Validação do Sexo
    while True:
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo in ("M", "F"):
            break
        print("ERRO! Por favor, digite apenas M ou F.")
        
    idade = int(input("Idade: "))
    soma_idade += idade
    
    pessoas.append({"nome": nome, "sexo": sexo, "idade": idade})

    # Validação do Continuar
    while True:
        resp = input("Quer continuar? [S/N]: ").strip().upper()
        if resp in ("S", "N"):
            break
        print("ERRO! Responda apenas S ou N.")
        
    if resp == "N":
        break
    
print("==" * 25)

# A) Quantidade de pessoas
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")

# B) Média de idade
media_idade = soma_idade / len(pessoas)
print(f"B) A média de idade do grupo é {media_idade:.2f} anos.")

# C) Lista de mulheres (Exibindo os nomes limpos)
mulheres = [p["nome"] for p in pessoas if p["sexo"] == "F"]
print("C) As mulheres cadastradas foram: ", end="")
if mulheres:
    print(", ".join(mulheres))
else:
    print("Nenhuma mulher cadastrada.")

# D) Pessoas com idade acima da média (Exibindo os detalhes de cada uma)
print("D) Lista de pessoas com idade acima da média:")
pessoas_acima = [p for p in pessoas if p["idade"] > media_idade]
if pessoas_acima:
    for p in pessoas_acima:
        print(f"   => nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']};")
else:
    print("   => Ninguém está acima da média.")

print("\n<<< ENCERRADO >>>")
