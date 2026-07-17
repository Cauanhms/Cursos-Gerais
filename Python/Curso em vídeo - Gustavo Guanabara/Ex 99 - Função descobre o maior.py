from time import sleep

def maior(*numeros):
    print("═" * 45)
    print("Analisando os valores fornecidos...")
    sleep(0.5)
    
    if len(numeros) == 0:
        print("Nenhum valor foi informado.")
    else:
        for numero in numeros:
            print(f"{numero} ", end="", flush=True)
            sleep(0.2)
        
        print(f"\nForam informados {len(numeros)} valores ao todo.")
        print(f"O maior valor informado foi o valor: {max(numeros)}")

maior(2, 9, 4, 5, 7, 1)
maior(8, 3, 6, 10, 2)
maior(1, 5)
maior(0)
maior()