# ===== DESAFIO 097 =====

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    tamanho = len(texto) + 4
    print("-" * tamanho)
    print(f"  {texto}  ")
    print("-" * tamanho)

escreva("Olá, Mundo!")
escreva("Python é incrível!")
escreva("Fazendo curso de Python com Gustavo Guanabara.")
