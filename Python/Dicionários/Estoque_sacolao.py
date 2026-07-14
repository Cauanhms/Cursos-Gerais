# =====================================================================
# BLOCO 1: BANCO DE DADOS E INFRAESTRUTURA DE ESTOQUE
# =====================================================================

# --- Sub-Bloco 1.1: Inventário de Frutas ---
estoque_frutas = {
    "banana":  {"preco": 5.99, "quantidade": 45, "unidade": "kg"},
    "maçã":    {"preco": 8.49, "quantidade": 30, "unidade": "kg"},
    "morango": {"preco": 7.50, "quantidade": 12, "unidade": "bandejas"},
    "uva":     {"preco": 9.90, "quantidade": 15, "unidade": "bandejas"},
    "laranja": {"preco": 4.20, "quantidade": 80, "unidade": "kg"},
    "melancia":{"preco": 12.00, "quantidade": 8, "unidade": "unidades"},
    "abacaxi": {"preco": 6.80, "quantidade": 14, "unidade": "unidades"}
}

# --- Sub-Bloco 1.2: Inventário de Verduras ---
estoque_verduras = {
    "alface":    {"preco": 3.50, "quantidade": 20, "unidade": "maços"},
    "tomate":    {"preco": 7.89, "quantidade": 35, "unidade": "kg"},
    "cenoura":   {"preco": 5.50, "quantidade": 25, "unidade": "kg"},
    "brocolis":  {"preco": 6.00, "quantidade": 10, "unidade": "maços"},
    "cebola":    {"preco": 4.99, "quantidade": 50, "unidade": "kg"},
    "batata":    {"preco": 6.40, "quantidade": 60, "unidade": "kg"},
    "espinafre": {"preco": 4.20, "quantidade": 15, "unidade": "maços"}
}

# --- Sub-Bloco 1.3: Unificação dos Dicionários (Visão Geral) ---
sacolao = {**estoque_frutas, **estoque_verduras}


# =====================================================================
# BLOCO 2: NÚCLEO OPERACIONAL (LOOP PRINCIPAL DO SISTEMA)
# =====================================================================
while True:
    
    # --- Sub-Bloco 2.1: Painel de Controle de Acesso (Login Geral) ---
    print("=="*10,"Sacolão","=="*10)
    print("Selecione o tipo de usuário: ")
    print("[ 1 ] - Usuário Comum")
    print("[ 2 ] - Administrador")
    tipouser = int(input("Opção: "))
    print("")

    # =================================================================
    # BLOCO 3: MÓDULO DO USUÁRIO COMUM (INTERFACE DE CLIENTE)
    # =================================================================
    if tipouser == 1:
        
        # --- Sub-Bloco 3.1: Menu de Opções do Cliente ---
        print("Selecione uma opção: ")
        print("[ 1 ] - Ver todos os produtos e estoque.")
        print("[ 2 ] - Fazer compras.")
        print("[ 3 ] - Sair.")
        escolhacomum = int(input("Escolha: "))
        print("")

        # --- Sub-Bloco 3.2: Consulta de Inventário Formatada ---
        if escolhacomum == 1:
            print("="*65)
            print(f"{'PRODUTO':<15} | {'PREÇO (R$)':<12} | {'QUANTIDADE':<12} | {'UNIDADE':<10}")
            print("-"*65)
            
            for produto, dados in sorted(sacolao.items()):
                print(f"{produto.capitalize():<15} | R$ {dados['preco']:<9.2f} | {dados['quantidade']:<12} | {dados['unidade'].capitalize():<10}")
                
            print("="*65 + "\n")

        # --- Sub-Bloco 3.3: Fluxo Completo de Vendas ---
        elif escolhacomum == 2:
            print("="*10 + " ÁREA DE COMPRAS " + "="*10)
            produto_desejado = input("Digite o nome do produto que deseja comprar: ").strip().lower()

            # ... Identificação do Item ...
            if produto_desejado in sacolao:
                preco_unitario = sacolao[produto_desejado]["preco"]
                estoque_disponivel = sacolao[produto_desejado]["quantidade"]
                unidade_medida = sacolao[produto_desejado]["unidade"]

                print(f"Produto encontrado! Preço: R$ {preco_unitario:.2f} por {unidade_medida.capitalize()} | Estoque atual: {estoque_disponivel} {unidade_medida.capitalize()}")
                qtd_comprar = int(input(f"Quantas unidades/medidas ({unidade_medida.capitalize()}) de {produto_desejado.title()} você quer? "))

                # ... Validação Física de Estoque ...
                if qtd_comprar <= estoque_disponivel:
                    valor_base = qtd_comprar * preco_unitario
                    valor_final = valor_base
                    detalhe_pagamento = ""
                    
                    # ... Sub-Processo: Menu de Checkout (Formas de Pagamento) ...
                    print("\nEscolha o método de pagamento: ")
                    print("[ 1 ] - À vista no dinheiro (10% de desconto)")
                    print("[ 2 ] - À vista no Pix / Débito ou Crédito (sem desconto)")
                    print("[ 3 ] - Parcelado em até 3x (sem juros)")
                    print("[ 4 ] - Parcelado em até 12x (acréscimo de 7.5% no valor final)")
                    forma_pagto = int(input("Opção: "))
                    
                    # ... Sub-Processo: Cálculo Financeiro Processual ...
                    if forma_pagto == 1:
                        valor_final = valor_base * 0.90
                        detalhe_pagamento = "Pago à vista no dinheiro com 10% de desconto."
                        
                    elif forma_pagto == 2:
                        detalhe_pagamento = "Pago à vista no Pix/Cartão."
                        
                    elif forma_pagto == 3:
                        while True:
                            parcelas = int(input("Em quantas vezes deseja parcelar (1 a 3)? "))
                            if 1 <= parcelas <= 3:
                                break
                            print("Opção inválida! Por favor, escolha um número de 1 a 3.")
                        val_parcela = valor_base / parcelas
                        detalhe_pagamento = f"Parcelado em {parcelas}x de R$ {val_parcela:.2f} sem juros."
                        
                    elif forma_pagto == 4:
                        valor_final = valor_base * 1.075
                        while True:
                            parcelas = int(input("Em quantas vezes deseja parcelar (4 a 12)? "))
                            if 4 <= parcelas <= 12:
                                break
                            print("Opção inválida! Por favor, escolha um número de 4 a 12.")
                        val_parcela = valor_final / parcelas
                        detalhe_pagamento = f"Parcelado em {parcelas}x de R$ {val_parcela:.2f} (com juros de 7.5%)."
                        
                    else:
                        print("⚠️ Opção de pagamento inválida! O valor será cobrado integralmente à vista.")
                        detalhe_pagamento = "Pago integralmente à vista (opção inválida selecionada)."

                    # ... Sub-Processo: Baixa Patrimonial e Emissão de Cupom Fiscal ...
                    sacolao[produto_desejado]["quantidade"] -= qtd_comprar
                    
                    print("\n" + "═"*40)
                    print(f"✅ COMPRA REALIZADA COM SUCESSO!")
                    print(f" Item: {qtd_comprar} {unidade_medida.capitalize()} de {produto_desejado.capitalize()}")
                    print(f" Valor Original: R$ {valor_base:.2f}")
                    print(f" Forma de Pagamento: {detalhe_pagamento}")
                    print(f" TOTAL A PAGAR: R$ {valor_final:.2f}")
                    print(f" Novo estoque de {produto_desejado.title()}: {sacolao[produto_desejado]['quantidade']} {unidade_medida.capitalize()}")
                    print("═"*40 + "\n")
                    
                else:
                    print(f"\n❌ Desculpe, não temos essa quantidade. Estoque máximo: {estoque_disponivel} {unidade_medida.capitalize()}")
            else:
                print("\n❌ Esse produto não está cadastrado no nosso sacolão. Volte em outro momento.")

        # --- Sub-Bloco 3.4: Rotina de Encerramento Voluntário ---
        elif escolhacomum == 3:
            print("="*10 + " VOLTE SEMPRE! " + "="*10)
            exit()

        else:
            print("❌ Opção inválida, escolha de 1 a 3.")


    # =================================================================
    # BLOCO 4: MÓDULO DO ADMINISTRADOR (SISTEMA DE GESTÃO)
    # =================================================================
    elif tipouser == 2:
        
        # --- Sub-Bloco 4.1: Gateway de Segurança (Autenticação Tripla) ---
        senha_correta = "adminsacolao230626"
        tentativas = 3
        autenticado = False

        while tentativas > 0:
            senha_digitada = input("Digite a senha de administrador: ")
            if senha_digitada == senha_correta:
                autenticado = True
                print("🔓 Acesso concedido!\n")
                break
            else:
                tentativas -= 1
                if tentativas > 0:
                    print(f"❌ Senha incorreta! Você tem mais {tentativas} tentativa(s).")
                
        if not autenticado:
            print("\n🛑 ACESSO BLOQUEADO! Número máximo de tentativas excedido.")
            exit()

        # --- Sub-Bloco 4.2: Painel de Controle Administrativo ---
        print("Selecione uma opção: ")
        print("[ 1 ] - Repor estoque.")
        print("[ 2 ] - Adicionar um produto.")
        print("[ 3 ] - Excluir um produto.")
        print("[ 4 ] - Sair.")
        escolhaadm = int(input("Opção: "))
        print("")

        # --- Sub-Bloco 4.3: Operação de Incremento de Estoque ---
        if escolhaadm == 1:
            print("="*10 + " REPOSIÇÃO DE ESTOQUE " + "="*10)
            produto_repor = input("Digite o nome do produto para repor: ").strip().lower()
            
            if produto_repor in sacolao:
                qtd_reposicao = int(input(f"Quantidade atual de {produto_repor.capitalize()} é {sacolao[produto_repor]['quantidade']} {sacolao[produto_repor]['unidade'].capitalize()}.\nQuanto deseja somar ao estoque? "))
                if qtd_reposicao > 0:
                    sacolao[produto_repor]["quantidade"] += qtd_reposicao
                    print(f"✅ Estoque atualizado! Novo estoque de {produto_repor.capitalize()}: {sacolao[produto_repor]['quantidade']} {sacolao[produto_repor]['unidade'].capitalize()}.\n")
                else:
                    print("❌ A quantidade deve ser maior que zero.\n")
            else:
                print("❌ Produto não localizado.\n")

        # --- Sub-Bloco 4.4: Operação de Inclusão de Novos Itens ---
        elif escolhaadm == 2:
            print("="*10 + " ADICIONAR NOVO PRODUTO " + "="*10)
            novo_produto = input("Nome do novo produto: ").strip().lower()
            
            if novo_produto in sacolao:
                print("❌ Este produto já existe no estoque! Use a opção de repor estoque.\n")
            else:
                novo_preco = float(input(f"Preço de venda para {novo_produto.capitalize()} (R$): "))
                nova_qtd = int(input("Quantidade inicial em estoque: "))
                nova_unidade = input("Unidade de medida (ex: Kg, Unidades, Bandejas, Maços): ").strip().lower()
                
                sacolao[novo_produto] = {
                    "preco": novo_preco,
                    "quantidade": nova_qtd,
                    "unidade": nova_unidade
                }
                print(f"✅ Produto {novo_produto.capitalize()} cadastrado com sucesso!\n")

        # --- Sub-Bloco 4.5: Operação de Descarte/Remoção de Itens ---
        elif escolhaadm == 3:
            print("="*10 + " EXCLUIR PRODUTO DO SISTEMA " + "="*10)
            produto_excluir = input("Nome do produto que deseja deletar permanentemente: ").strip().lower()
            
            if produto_excluir in sacolao:
                confirmacao = input(f"Tem certeza que deseja deletar {produto_excluir.capitalize()}? [S/N]: ").strip().upper()
                if confirmacao == 'S':
                    del sacolao[produto_excluir]
                    print(f"✅ {produto_excluir.capitalize()} foi removido do sistema.\n")
                else:
                    print("⚠️ Operação cancelada pelo administrador.\n")
            else:
                print("❌ Produto não cadastrado no sistema.\n")

        # --- Sub-Bloco 4.6: Encerramento de Sessão Gerencial ---
        elif escolhaadm == 4:
            print("="*10 + " SESSÃO ADMINISTRATIVA ENCERRADA " + "="*10)
            exit()
            
        else:
            print("❌ Opção inválida, escolha de 1 a 4.")
            
    # --- Sub-Bloco 2.2: Tratamento de Exceção do Login ---
    else:
        print("❌ Tipo de usuário inválido! Digite 1 ou 2.")