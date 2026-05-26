# ===== DESAFIO 008 =====

# Escreva um programa que leia uma distância em metros e a exiba convertida em todas as métricas.
metros = float(input('Digite uma distância em metros: '))
print(f'A distância de {metros} metros corresponde a: {metros / 1000:.2f}km')
print(f'A distância de {metros} metros corresponde a: {metros / 100:.2f}hm')
print(f'A distância de {metros} metros corresponde a: {metros / 10:.2f}dam')
print(f'A distância de {metros} metros corresponde a: {metros * 10:.2f}dm')
print(f'A distância de {metros} metros corresponde a: {metros * 100:.2f}cm')
print(f'A distância de {metros} metros corresponde a: {metros * 1000:.2f}mm')
