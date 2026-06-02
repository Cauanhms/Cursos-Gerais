# Nosso "banco de dados" de usuários

# 1º Exercício: Criar uma lista para armazenar os dados dos usuários

identificacao = 0

usuarios = [
    ["Alice", "alice@gmail.com", 30],
    ["Sapo", "saponaolavaope@gmail.com", 7],
    ["Ladrão", "luisinaciolula@gmail.com", 78],
    ["Pessoa", "anonimato@gmail.com", 100],
    ["Ford KA", "fordka@gmail.com", 29]
]

print("\n")
print("=="*10,"Todos os usuários registrados:","=="*10)
print("\n")
for usuario in range(len(usuarios)):
    identificacao += 1
    nome = usuarios[usuario][0]
    email = usuarios[usuario][1]
    idade = usuarios[usuario][2]
    print (f"ID usuário: {identificacao}    | Nome: {nome}  | Email: {email}    | Idade: {idade}")

# 2º Exercício usa uma variável para armazenar o primeiro usuário e o print para exibir este usuário

print("\n")
print("=="*25)
print("Segundo exercício:\n")
primeiro_user = usuarios[0]
print(f"Primeiro usuário: {primeiro_user}")

# 3º Exercício: Acesse e exiba o nome do segundo usuário definido na lista, somente o "Nome". Crie uma variável.

print("\n")
print("=="*25)
print("Terceiro exercício:\n")
nome_segundo_user = usuarios[1][0]
print(f"O nome do segundo usuário é: {nome_segundo_user}")

escolha_user_novo = input("Você deseja adicionar um novo usuário: (S/N)\nEscolha: ").strip().upper()
if escolha_user_novo == "S":
    nome_novo = str(input("\nNome do novo usuário: "))
    email_novo = str(input("Email do novo usuário: "))
    idade_nova = int(input("A idade do novo usuário: "))

    usuario_novo = [nome_novo, email_novo, idade_nova]

    usuarios.append(usuario_novo)
    