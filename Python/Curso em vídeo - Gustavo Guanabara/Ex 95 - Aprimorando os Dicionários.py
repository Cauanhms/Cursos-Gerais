# ===== DESAFIO 095 =====

# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep

# Lista para armazenar os jogadores
jogadores = []

while True:
    # Dicionário para armazenar os dados de cada jogador
    jogador = {'nome': input("Nome do jogador: ").strip()}
    
    # Obtendo o número de partidas jogadas
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    
    # Obtendo o número de gols em cada partida
    gols = []
    for i in range(partidas):
        print(f'\n===== Partida {i + 1}: =====')
        gols.append(int(input(f'Quantos gols na partida {i + 1}?\nNº de gols: ')))
    
    # Salvando os dados no dicionário do jogador
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    
    jogadores.append(jogador)
    
    continuar = input("Deseja cadastrar outro jogador? [S/N]: ").strip().upper()
    if continuar == 'N':
        break
  
# Mostrando o resumo geral dos jogadores cadastrados  
print("\n=== RESUMO DOS JOGADORES ===")
print(f"{'Código':<6}{'Nome':<15}{'Gols':<20}{'Total':<6}")
print("-" * 50)
for indice, jogador in enumerate(jogadores):
    print(f"{indice:<6}{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total']:<6}")
    print("-" * 50)

# Sistema de detalhes do aproveitamento de cada jogador    
while True:
    detalhes = int(input("Digite o Código do jogador para ver os detalhes (999 para sair): "))
    if detalhes == 999:
        print("Saindo do sistema...")
        sleep(1.5)
        break
    
    elif detalhes < len(jogadores):
        jogador = jogadores[detalhes]
        print(f"Detalhes do jogador {jogador['nome']}:")
        for i, gols in enumerate(jogador['gols']):
            print(f"  Partida {i + 1}: {gols} gols")
            
    else:
        print("Código inválido. Tente novamente.")

print("<<< ENCERRADO >>>")
