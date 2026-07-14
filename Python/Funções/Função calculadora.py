# Funções com *args - calculadora flexível

def estatisticas(*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Total: {total} | Média: {media:.2f} | Máx: {maximo} | Mín: {minimo}")

# Tuplas
estatisticas(10,20.30)
estatisticas(50, 68, 80, 90, 46)
estatisticas(70,89,49)

# Lista
lista = [80, 90, 95]
estatisticas(lista)