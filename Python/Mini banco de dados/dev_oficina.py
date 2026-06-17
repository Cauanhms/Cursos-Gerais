from datetime import date

# --- CONFIGURAÇÕES E VARIÁVEIS GLOBAIS ---
ano_atual = date.today().year
oficina_geral = []  # Nosso "banco de dados" simulado em memória


# --- FUNÇÕES DO SISTEMA ---

def cadastrar_ordem_servico():
    """
    Captura os dados do cliente, veículo, quilometragem e lança as peças/serviços,
    gerando uma nova Ordem de Serviço (O.S.).
    """
    print("\n" + "="*30)
    print("     NOVA ORDEM DE SERVIÇO     ")
    print("="*30)

    # 1. Dados Básicos
    cliente = input("Nome do cliente: ").strip()
    modelo_carro = input("Modelo do veículo: ").strip()

    # 2. Validação do Ano do Veículo
    while True:
        try:
            ano_carro = int(input("Ano do veículo (AAAA): "))
            if 1900 <= ano_carro <= ano_atual:
                break
            else:
                print(f"Erro: O ano deve estar entre 1900 e {ano_atual}.")
        except ValueError:
            print("Erro: Digite um ano válido com 4 dígitos (Ex: 2020).")

    # 3. Validação da Quilometragem
    while True:
        try:
            quilometragem = int(input("Quilometragem atual: "))
            if quilometragem >= 0:
                break
            print("A quilometragem não deve ser negativa.")
        except ValueError:
            print("Erro: A quilometragem deve ser um número inteiro.")

    # 4. Verificação de Alerta Preventivo
    necessita_revisao_completa = False
    if quilometragem > 10000 or ano_carro < (ano_atual - 5):
        print("\n⚠️  Alerta do sistema: Veículo necessita de revisão preventiva!")
        necessita_revisao_completa = True
    else:
        print("\n✅ Status: Manutenção de rotina.")

    # 5. Lançamento de Peças e Serviços
    lista_pecas = []
    total_orcamento = 0.00

    print("\n--- LANÇAMENTO DE PEÇAS E SERVIÇOS ---")
    while True:
        peca = input('Nome da peça/serviço (ou "fim" para encerrar): ').strip()
        if peca.lower() == "fim":
            break
        
        try:
            preco = float(input(f"Preço de [{peca}]: R$ "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            
            lista_pecas.append({"nome": peca, "preco": preco})
            total_orcamento += preco
        except ValueError:
            print("Erro: Preço inválido! Item desconsiderado. Tente novamente.")

    # 6. Estruturação dos Dados (Dicionário)
    ordem_servico = {
        "cliente": cliente,
        "veiculo": modelo_carro,
        "ano": ano_carro,
        "km": quilometragem,
        "alerta_revisao": necessita_revisao_completa,
        "itens": lista_pecas,
        "total": total_orcamento,
        "status": "Em Aberto"
    }

    # 7. Salvando no "Banco de Dados" global
    oficina_geral.append(ordem_servico)
    print(f"\n✨ Ordem de serviço para {cliente} gerada com sucesso!")


def listar_todas_as_ordens():
    """
    Varre a lista global e exibe de forma limpa e estruturada
    todos os dados de cada Ordem de Serviço cadastrada.
    """
    print("\n" + "==" * 20)
    print("       RELATÓRIO GERAL DA OFICINA       ")
    print("==" * 20)

    if not oficina_geral:
        print("Nenhum veículo em manutenção no momento.")
        return

    # O "for" percorre a lista de dicionários
    for indice, ordem in enumerate(oficina_geral, 1):
        print(f"\n🛠️  #OS: {indice} | Cliente: {ordem['cliente']}")
        print(f"   Veículo: {ordem['veiculo']} ({ordem['ano']}) | KM: {ordem['km']}")
        print(f"   Revisão Crítica: {'⚠️  SIM' if ordem['alerta_revisao'] else '✅ NÃO'}")
        print(f"   Status: {ordem['status']}")
        print("   Itens Trocados / Serviços:")
        
        if not ordem['itens']:
            print("     - Nenhum item cadastrado.")
        else:
            for item in ordem['itens']:
                print(f"     • {item['nome']}: R$ {item['preco']:.2f}")
                
        print(f"   💰 TOTAL ORÇAMENTO: R$ {ordem['total']:.2f}")
        print("-" * 40)


# --- MENU PRINCIPAL DO PROGRAMA ---

def menu():
    while True:
        print("\n" + "="*35)
        print("    ⚙️  OFICINA MECÂNICA CHARURI  ⚙️    ")
        print("="*35)
        print("[ 1 ] Cadastrar Nova Ordem de Serviço")
        print("[ 2 ] Listar Todas as Ordens (Relatório)")
        print("[ 0 ] Sair do Sistema")
        print("="*35)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_ordem_servico()
        elif opcao == "2":
            listar_todas_as_ordens()
        elif opcao == "0":
            print("\nEncerrando o sistema da Oficina Charuri. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Por favor, escolha uma opção do menu.")


# Executa o programa se este arquivo for o principal
if __name__ == "__main__":
    menu()
    