from random import randint

jogador = {}
partidas = []

jogador['nome'] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, total):
    print(f"============ {c+1}ª partida ==============")
    gols = int(input("Quantos gols na partida? "))
    assistencias = int(input("Quantas assistências na partida? "))
    partidas.append({'gols': gols, 'assistências': assistencias})
    
jogador['partidas'] = partidas
jogador['total de gols'] = sum(p['gols'] for p in partidas)
jogador['total de assistências'] = sum(p['assistências'] for p in partidas)

print("\n" + "=" * 50)
print(f" DICIONÁRIO COMPLETO: {jogador}")
print("=" * 50)

for chave, valor in jogador.items():
    if chave != 'partidas':
        print(f"{chave.upper():<22}: {valor}")
        
print("=" * 50)
print(f" O aproveitamento de {jogador['nome']}:")
print("=" * 50)

for indice, partida in enumerate(jogador['partidas']):
    g_gols = "gol" if partida['gols'] == 1 else "gols"
    a_ast = "assistência" if partida['assistências'] == 1 else "assistências"
    
    print(f"   => Na partida {indice + 1}, fez {partida['gols']} {g_gols} e {partida['assistências']} {a_ast}.")

print("=" * 50)
t_gols = "gol" if jogador['total de gols'] == 1 else "gols"
t_ast = "assistência" if jogador['total de assistências'] == 1 else "assistências"
print(f"Foi um total de {jogador['total de gols']} {t_gols} e {jogador['total de assistências']} {t_ast} em {total} jogos!")
print(f"Total de participações em gols: {jogador['total de gols'] + jogador['total de assistências']}")
print(f"Média de participações de gol: {(jogador['total de gols'] + jogador['total de assistências']) / total:.2f}")
print("=" * 50)
