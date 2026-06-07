# ===== DESAFIO 067 =====

# Faça um programa que mostre a tabuada de vários números. Um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input("Quer ver a tabuada de qual valor (valor negativo para o programa): "))
    print("=="*20)
    
    if numero < 0:
        break
    
    for vezes in range(1,11):
        print(f"{numero} x {vezes} = {numero * vezes}")
    print("=="*20)
    
print("\nPrograma de tabuada finalizado com sucesso!")
