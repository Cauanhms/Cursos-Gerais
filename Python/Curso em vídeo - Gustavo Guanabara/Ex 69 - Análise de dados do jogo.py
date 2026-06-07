total18 = totalhomem = totalmulher20 = 0
cont = 1

while True:
    print(f"\n{'=' * 5} CADASTRO DA {cont}ª PESSOA {'=' * 5}")
    
    idade = int(input("Idade: "))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: (M/F) ')).strip().upper()[0]
    
    if idade >= 18:
        total18 += 1
        
    if sexo == 'M':
        totalhomem += 1
        
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
        
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    
    cont += 1
    
    if resposta == 'N':
        break

print(f"\n{'=' * 30}")
print(f'Total de pessoas com mais de 18 anos: {total18}')        
print(f'Ao todo temos {totalhomem} homens cadastrados.')
print(f'E temos {totalmulher20} mulheres com menos de 20 anos.')
print(f"{'=' * 30}")
