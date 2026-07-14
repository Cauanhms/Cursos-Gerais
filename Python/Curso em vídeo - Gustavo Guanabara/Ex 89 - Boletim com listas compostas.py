from time import sleep

exercicio = "Boletim Escolar com Listas Compostas"

print("==" * 20)
print(f"{exercicio:^40}")
print("==" * 20)

ficha = []
contador = 0

while True:
    print(f"--------------- {contador + 1}º Aluno ---------------")
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    contador += 1
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
    
print("==" * 20)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("==" * 20)

for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
    
while True:
    print("==" * 20)
    opcao = int(input("Mostrar notas de qual aluno? (-1 interrompe)\nIndice: "))
    
    if opcao == -1:
        print("FINALIZANDO...")
        sleep(1)
        break
    
    if 0 <= opcao < len(ficha):
        print(f"Notas de {ficha[opcao][0]} são {ficha[opcao][1]}")
    else:
        print("Aluno não encontrado. Tente novamente.")
        
print("<<< VOLTE SEMPRE >>>")
