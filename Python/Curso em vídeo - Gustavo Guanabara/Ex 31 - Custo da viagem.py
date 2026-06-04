# ===== DESAFIO 031 =====

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input("Qual é a distância da viagem em Km: "))
if distancia <= 200:
    preco = distancia * 0.50
    texto = (f"O preço da passagem para a viagem de {distancia}Km é de R${preco:.2f}")
    texto_br = texto.replace(".", ",")
    print(f'{texto_br}.')
    
else:
    preco = distancia * 0.45
    txt = (f"O preço da passagem para a viagem de {distancia}Km é de R${preco:.2f}")
    txt_virugla = txt.replace(".", ",")
    print(f'{txt_virugla}.')
    