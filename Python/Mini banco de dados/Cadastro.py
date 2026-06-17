def cadastrar_funcionario():
    print("==" * 20)
    print("Cadastro de Funcionários")
    print("==" * 20)

    nome = input("Nome do funcionário: ").strip()

    setores_validos = ["Jurídico", "Marketing", "TI", "Vendas"]
    while True:
        setor = input("Setor (Jurídico/Marketing/TI/Vendas): ").strip()
        
        if setor.lower() == "ti":
            setor = "TI"
        else:
            setor = setor.title()

        if setor in setores_validos:
            break
        else:
            print("❌ Setor inválido! Por favor, escolha uma das opções da lista.")

    while True:
        try:
            salario = float(input("Salário (Ex: 1450.00): R$"))
            break
        except ValueError:
            print("❌ Valor inválido! Digite apenas números e use ponto para os centavos.")

    cargos_validos = ["Gerente", "Analista"]
    while True:
        cargo = input("Cargo (Gerente/Analista): ").strip().title()
        if cargo in cargos_validos:
            break
        else:
            print("❌ Cargo inválido! Escolha entre 'Gerente' ou 'Analista'.")

    while True:
        try:
            bonus = float(input("Bônus (Ex: 850.00): R$"))
            break
        except ValueError:
            print("❌ Valor inválido! Digite apenas números e use ponto para os centavos.")

    linha = f"{setor}| {nome}| {salario:.2f}| {cargo}| {bonus:.2f}\n"

    with open("funcionarios.txt", "a", encoding="utf-8") as arquivo: 
        arquivo.write(linha)

    print("\nFuncionário cadastrado com sucesso!")
    print('Dados salvos em "funcionarios.txt"')
    return {"Setor": setor, "Nome": nome, "Salário": salario, "Cargo": cargo, "Bônus": bonus}

novo_funcionario = cadastrar_funcionario()
print("\nDados cadastrados:", novo_funcionario)
