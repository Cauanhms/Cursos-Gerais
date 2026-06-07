# Lista de times em ordem de colocação (Temporada 2026 - Atualizada)
times = (
    'Flamengo', 'Palmeiras', 'Botafogo', 'São Paulo', 'Internacional', 
    'Atlético-MG', 'Cruzeiro', 'Bahia', 'Fortaleza', 'Grêmio', 
    'Fluminense', 'Vasco da Gama', 'Corinthians', 'Athletico-PR', 'Bragantino', 
    'Atlético-GO', 'Juventude', 'Criciúma', 'Vitória', 'Cuiabá'
)

print(f"{'='*60}")
print(f"{'BRASILEIRÃO 2026 - TABELA ATUAL':^60}")
print(f"{'='*60}")

# Exibição dos Times
for pos, time in enumerate(times):
    print(f"{pos + 1:02}º Lugar: {time}")

print(f"\n{'='*30}")
print(f"{'CLASSIFICAÇÃO POR ZONAS':^60}")
print(f"{'='*30}")

# A) Libertadores (G6)
print(f"\033[1;32mLIBERTADORES (Fase de Grupos):\033[m {times[0:6]}")

# B) Pré-Libertadores (G8)
print(f"\033[1;33mPRÉ-LIBERTADORES:\033[m {times[6:8]}")

# C) Sul-Americana (G12)
print(f"\033[1;36mSUL-AMERICANA:\033[m {times[8:12]}")

# D) Rebaixados (Z4)
print(f"\n\033[1;31mREBAIXADOS (Z4):\033[m {times[-4:]}")

print(f"\n{'='*30}")
print(f"Times em ordem alfabética: \n{sorted(times)}")
print(f"{'='*30}")
