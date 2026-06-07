# ===== DESAFIO 065 =====

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar.

resposta = "S"
soma = quantidade = media = 0

while resposta in "Ss":
    print(f"{'==' * 10} {quantidade + 1}º Número: {'==' * 10}")
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1
    
    if quantidade == 1:
        maior = menor = numero
        
    else:
        if numero > maior:
            maior = numero
            
        if numero < menor:
            menor = numero
            
    resposta = str(input("Quer continuar (S/N): ")).strip()
    
media = soma / quantidade

if quantidade > 1:
    print(f"\nVocê digitou {quantidade} números e a média deles foi {media:.2f}.")
    print(f"O maior número registrado foi {maior} e o menor foi {menor}.")
        
else:
    print(f"\nVocê digitou um único valor que foi: {numero}.")