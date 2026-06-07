# ===== DESAFIO 080 =====

# Crie um programa onde o usário possa digitar cinco valores númericos e cadastrados em uma lista. Já na posição correta de inserção (sem o uso do .sort()). No final mostre a lista ordenada na tela.

lista = []

for contagem in range(0, 5):
    numero = int(input("\nDigite um valor: "))
    
    if contagem == 0 or numero > lista[-1]:
        lista.append(numero)
        print("Adicionado ao final da lista...")
        
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao+1} da lista...")
                break
            posicao += 1

print("==" * 20)
print(f"Os valores digitados em ordem: {lista}")
