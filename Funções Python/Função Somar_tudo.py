#main

#Jeito 1
def somar_tudo(*numeros):
    somar = 0
    for numero in numeros:
        somar = somar + numero
    return f"A soma de todos os seus números deu: {somar}"

resultado_1 = somar_tudo(500,900,800,745,965)
print("\nJeito 1")
print(resultado_1)

print("=="*25)

#Jeito 2
def sum_all(*numeros):
    return f"A soma de todos os seus números deu: {sum(numeros)}"

resultado_2 = sum_all(500,900,800,100,200)
print("Jeito 2")
print(resultado_2)