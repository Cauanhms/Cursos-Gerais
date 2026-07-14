#main

#Criando o 1º Dicionário
produto = {"nome":"Teclado",
            "preco": 150,
            "em_estoque": True}

# Acessando um valor
print("\n",produto["nome"])

# Modificando um valor
produto ["preco"] = 135.00

# Adicionando um novo par
produto["quantidade"] = 10

print(produto)

print("==" * 25,)

#Criando o 2º Dicionário
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# Acessando um valor
print(carro["modelo"]) # Saída: Mustang

# Adicionando/Alterando um valor
carro["cor"] = "Vermelho"
carro["ano"] = 2020

print(carro)
print("\n")
# Saída: {'marca': 'Ford', 'modelo': 'Mustang', 'ano': 2020, 'cor': 'Vermelho'}