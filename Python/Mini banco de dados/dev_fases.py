# ==============================================================================
# EVOLUÇÃO DO CÓDIGO: DO INPUT SIMPLES AO SISTEMA COMPLETO
# ==============================================================================

# ------------------------------------------------------------------------------
# EX 1 / FASE 1: Variável simples e Input
# ------------------------------------------------------------------------------
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}")


# ------------------------------------------------------------------------------
# FASE 2: Lista e Laço While (Guardando vários nomes)
# ------------------------------------------------------------------------------
# nomes = []
# while True:
#     nome = input('Digite um nome (ou "sair" para terminar): ').lower().strip()
#     if nome == "sair":
#         break
#     nomes.append(nome.capitalize())
#
# print("")
# for nome in nomes:
#     print(nome)


# ------------------------------------------------------------------------------
# FASE 3: Busca e Enumeração (Simulando um Banco de Dados)
# ------------------------------------------------------------------------------
# busca = input("Pesquisar nome: ").strip().capitalize()
# if busca in nomes:
#     print(f"{busca} encontrado")
# else:
#     print(f"{busca} não está na lista")
#
# for indice, nomenclatura in enumerate(nomes, 1):
#     print(f"{indice}. {nomenclatura}")


# ------------------------------------------------------------------------------
# FASE 4: Salvar e Carregar Arquivo de Texto (Persistência)
# ------------------------------------------------------------------------------
# with open("nomes.txt", "w", encoding="utf-8") as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + "\n")
# print("Nomes salvos com sucesso!")
#
# with open("nomes.txt", "r", encoding="utf-8") as arquivo:
#     nomes_carregados = arquivo.read().splitlines()
# print("Nomes carregados: ", nomes_carregados)


# ------------------------------------------------------------------------------
# FASE 5: Tratamento de Erros e Validação Básica
# ------------------------------------------------------------------------------
# try:
#     with open("nomes.txt", "r", encoding="utf-8") as f:
#         nomes = f.read().splitlines()
# except FileNotFoundError:
#     print("Arquivo não encontrado. Iniciando vazio.")
#     nomes = []
#
# def validar_nome(nome):
#     if not nome.strip():
#         raise ValueError("Nome não pode ser vazio!")
#     return nome.strip().capitalize()
#
# try:
#     nome = validar_nome(input("Nome: "))
#     nomes.append(nome)
# except ValueError as e:
#     print(f"Erro: {e}")


# ==============================================================================
# FASE 6: Organização com Funções (Código Ativo)
# ==============================================================================

ARQUIVO = "nomes.txt"

def carregar_nomes():
    """Tenta ler o arquivo TXT. Se não existir, retorna uma lista vazia."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    
def salvar_nomes(nomes):
    """Grava a lista de nomes no arquivo de texto."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")

def adicionar_nome(nomes, nome):
    """Valida o nome e adiciona na lista com formatação correta."""
    if not nome.strip():
        raise ValueError("O nome não pode ser vazio.")
    nomes.append(nome.strip().capitalize())

def buscar_nomes(nomes, busca):
    """Verifica a existência do nome ignorando variações de espaços/letras."""
    return busca.strip().capitalize() in nomes

def listar_nomes(nomes):
    """Exibe todos os nomes salvos de forma organizada."""
    if not nomes:
        print("\n[!] A lista está vazia no momento.")
        return
    print("\n==================================")
    print("         NOMES CADASTRADOS        ")
    print("==================================")
    for i, n in enumerate(nomes, 1):
        print(f"  {i}. {n}")
    print("==================================")


# ------------------------------------------------------------------------------
# FASE 7: Interface com Menu Interativo (Fluxo Principal)
# ------------------------------------------------------------------------------

def menu():
    """Exibe o menu formatado na tela."""
    print("\n==================================")
    print("       CADASTRO DE NOMES          ")
    print("==================================")
    print(" 1. Adicionar Nome")
    print(" 2. Listar Nomes")
    print(" 3. Buscar Nome")
    print(" 4. Salvar e Sair")
    print("==================================")
    return input("Escolha uma opção: ").strip()

if __name__ == "__main__":
    nomes = carregar_nomes()

    while True:
        opcao = menu()
        
        if opcao == "1":
            print("\n>>> AÇÃO: ADICIONAR NOME")
            print("----------------------------------")
            try:
                novo_nome = input("Digite o nome: ")
                adicionar_nome(nomes, novo_nome)
                print("----------------------------------")
                print(f"[SUCESSO] '{novo_nome.strip().title()}' foi adicionado!")
            except ValueError as e:
                print("----------------------------------")
                print(f"[ERRO] {e}")

        elif opcao == "2":
            # A própria função listar_nomes já possui sua estilização visual
            listar_nomes(nomes)

        elif opcao == "3":
            print("\n>>> AÇÃO: BUSCAR NOME")
            print("----------------------------------")
            busca = input("Digite o nome para buscar: ")
            achou = buscar_nomes(nomes, busca)
            print("----------------------------------")
            if achou:
                print(f"[RESULTADO] '{busca.strip().title()}' está na lista!")
            else:
                print(f"[RESULTADO] '{busca.strip().title()}' NÃO foi encontrado.")

        elif opcao == "4":
            print("\n>>> ENCERRANDO O SISTEMA...")
            print("----------------------------------")
            salvar_nomes(nomes)
            print("[OK] Dados salvos em 'nomes.txt'.")
            print("Até logo!")
            print("----------------------------------")
            break
            
        else:
            print("\n----------------------------------")
            print("[AVISO] Opção inválida! Escolha de 1 a 4.")
            print("----------------------------------")