# **Kwargs - argumentos nomeados variáveis
# Captura qualquer quantidade de argumentos como um dicionário.

def exibir_info(**dados):       # **kwargs vira dicionário
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(Nome="Carlos", Idade=30, Cidade="SP", Partido="Bolsonaro")
