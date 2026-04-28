#main

def saudacao(nome, mensagem = "Seja bem vindo(a)!"):
    print(f"\nOlá {nome}, {mensagem}")

def cadastro_user(nome, idade: int, admin=False):
    print(f"\nNome: {nome}    |     Idade: {idade}     |   Administrador: {admin}")

saudacao("Cauan")
cadastro_user("Python", 35)