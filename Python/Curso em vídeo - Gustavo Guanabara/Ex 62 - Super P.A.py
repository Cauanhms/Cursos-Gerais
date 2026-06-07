print("==" * 15)
print("Super gerador de P.A")
print("==" * 15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da P.A: "))

termo = primeiro
contagem = 1
total_mostrado = 0
mais = 10 

while mais != 0:
    total_mostrado += mais
    
    while contagem <= total_mostrado:
        print(f"{termo}", end="")
        
        if contagem == total_mostrado:
            print(".")
        else:
            print(" -> ", end="")
            
        termo += razao
        contagem += 1
        
    print("PAUSA!")
    mais = int(input("\nQuantos termos você quer mostrar a mais: "))

print(f"\nFIM, P.A finalizada com o total de {total_mostrado} termos mostrados.")
