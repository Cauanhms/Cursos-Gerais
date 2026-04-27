#main 

def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = calcular_media(n1,n2,n3)
print("A média é: ", media)