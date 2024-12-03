# Lucas Henrique Ferreira de Oliveira   
# Análise e Desenvolvimento de Sistemas


import json


# Função para salvar os dados no arquivo JSON.
def salvar_dados(dados_de_cadastro):
    with open('dados_cadastro.json', 'w') as arquivo:
        json.dump(dados_de_cadastro, arquivo, indent=4)


# Função para recuperar os dados do arquivo JSON.
def recuperar_dados():
    try:
        with open('dados_cadastro.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {'estudante': [], 'turma': [], 'disciplina': [], 'professor': [], 'matrícula': []}


# Função do menu principal.
def menu_principal():
    while True:  
        print("_" * 45)
        print('\nBem-vindo(a) ao sistema de cadastros!\n')
        print('Escolha uma opção:\n')
        print(' [1]  Estudantes')
        print(' [2]  Turmas')
        print(' [3]  Disciplinas')
        print(' [4]  Professores')
        print(' [5]  Matrículas')
        print(' [6]  Sair')
        print("_" * 45)
        try:
            opcao01 = int(input("\nPor favor, digite uma opção válida: "))
            if opcao01 in range(1, 7): 
                print(f"\nVocê escolheu a opção {opcao01}.")
                return opcao01
            else:
                print("\nOpção inválida. Escolha uma opção entre 1 e 6.")
        except ValueError:
            print("\nEntrada inválida! Por favor, digite um número inteiro entre 1 e 6.")


# Função do menu secundário(operações).
def menu_secundario():
    while True:  
        print("_" * 45)
        print('\n [1]  Incluir ') 
        print(' [2]  Listar ')
        print(' [3]  Atualizar ')
        print(' [4]  Excluir ')
        print(' [5]  Voltar ao menu principal\n')
        print("_" * 45)
        try:
            opcao02 = int(input("\nPor favor, digite uma opção válida: "))
            if opcao02 in range(1, 6): 
                print(f"\nVocê escolheu a opção {opcao02}.")
                return opcao02
            else:
                print("\nOpção inválida. Escolha uma opção entre 1 e 5.")
        except ValueError:
            print("\nEntrada inválida! Por favor, digite um número inteiro entre 1 e 5.")


# Função para realizar os cadastros.
def realizar_cadastros(tipo_de_dado):
    print(f"\nOpção cadastrar {tipo_de_dado} selecionada!\n")
    nome = input(f"\nDigite o nome do {tipo_de_dado} a ser cadastrado: ")
    while True:
        try:
            codigo = int(input(f"Digite o codigo do {tipo_de_dado}: "))
            break
        except ValueError:
            print("O codigo deve ser um número inteiro. Tente novamente.")
            
    # Estudante e professor, pedimos o nome, codigo e CPF.
    if tipo_de_dado in ['Estudante', 'Professor']:
        while True:
            cpf = input(f"Digite o CPF dos {tipo_de_dado}:(11 dígitos) ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print("O CPF deve ter exatamente 11 dígitos numéricos.")
        dados_de_cadastro = {
            "nome": nome,
            "codigo": codigo,
            "cpf": cpf 
        }
    else:
        dados_de_cadastro = {
            "nome": nome,
            "codigo": codigo
        }
    print(f"\nCadastro de {tipo_de_dado} realizado com sucesso!")
    return dados_de_cadastro


# Função para listar os dados cadastrados.
def listar_cadastros(dados_de_cadastro, tipo_de_dado, exibir_mensagem=True):
    if exibir_mensagem:  
        print(f"\nOpção listar {tipo_de_dado} selecionada!\n")
    if not dados_de_cadastro[tipo_de_dado]:  
        print(f"\nNão há cadastro de {tipo_de_dado} ativo.")
    else:
        print(f"\nSegue abaixo os cadastros de {tipo_de_dado.capitalize()}:\n")
        for item in dados_de_cadastro[tipo_de_dado]:
            print(item)


# Função para editar os dados dos cadastros.
def editar_cadastros(dados_de_cadastro, tipo_de_dado):
    print(f"\nOpção editar {tipo_de_dado} selecionada!\n")
    if not dados_de_cadastro[tipo_de_dado]:
        print(f"\nNão há cadastro de {tipo_de_dado} para edição.")
        return
    while True:
        listar = input(f"\nDeseja ver a lista de {tipo_de_dado} antes de editar? (s/n): ").strip().lower()
        if listar in ['s', 'n']:
            break
        print("\nPor favor, digite a opção (s) para ver a lista ou (n) para não visualizar.")
    if listar == 's':
        listar_cadastros(dados_de_cadastro, tipo_de_dado, exibir_mensagem=False)
    try:
        codigo_para_editar = int(input(f"\nDigite o código de {tipo_de_dado} que deseja editar: "))
    except ValueError:
        print("Código inválido, digite um código válido.")
        return
    for item in dados_de_cadastro[tipo_de_dado]:
        if item["codigo"] == codigo_para_editar:
            nome_novo = input(f"Digite o novo nome de {tipo_de_dado}: ")
            while True:
                try:
                    codigo_novo = int(input(f"Digite o novo código de {tipo_de_dado}: "))
                    break
                except ValueError:
                    print("O código deve ser um número inteiro.")
            item["nome"] = nome_novo
            item["codigo"] = codigo_novo

            # Atualizar CPF apenas para Estudantes e Professores
            if tipo_de_dado in ['estudante', 'professor']:
                while True:
                    cpf_novo = input(f"Digite o novo CPF do {tipo_de_dado} (11 dígitos): ")
                    if cpf_novo.isdigit() and len(cpf_novo) == 11:
                        item["cpf"] = cpf_novo
                        break
                    else:
                        print("O CPF deve ter exatamente 11 dígitos numéricos.")
            print(f"\nOs dados de cadastro de {tipo_de_dado.capitalize()} foram atualizados com sucesso!")
            return
        
    print(f"\n{tipo_de_dado.capitalize()} com código {codigo_para_editar} não encontrado, voltando ao menu de operações.")


# Função para excluir dados dos cadastros.
def excluir_cadastros(dados_de_cadastro, tipo_de_dado):
    print(f"\nOpção excluir {tipo_de_dado} selecionada!\n")
    if not dados_de_cadastro[tipo_de_dado]:
        print(f"Não há cadastro de {tipo_de_dado} para excluir.")
        return
    while True:
        listar = input(f"Deseja ver a lista de {tipo_de_dado} antes de excluir? (s/n): ").strip().lower()
        if listar in ['s', 'n']:
            break
        print("Por favor, digite a opção (s) para ver a lista ou (n) para não visualizar!")
    if listar == 's':
        listar_cadastros(dados_de_cadastro, tipo_de_dado, exibir_mensagem=False)
    try:
        codigo_excluir = int(input(f"\nDigite o código de {tipo_de_dado} que deseja excluir: "))
    except ValueError:
        print("Código inválido, digite um código válido")
        return
    for item in dados_de_cadastro[tipo_de_dado]:
        if item["codigo"] == codigo_excluir:
            dados_de_cadastro[tipo_de_dado].remove(item)
            print(f"\n{tipo_de_dado.capitalize()} com código {codigo_excluir} excluído com sucesso!")
            return
        
    print(f"\n{tipo_de_dado.capitalize()} com código {codigo_excluir} não encontrado, voltando ao menu de operações.")


# Função principal.
def funcao_principal():
    
    dados_de_cadastro = recuperar_dados()

    while True:
        opcao_primaria = menu_principal()

        if opcao_primaria == 1:
            tipo = "estudante"
        elif opcao_primaria == 2:
            tipo = "turma"
        elif opcao_primaria == 3:
            tipo = "disciplina"
        elif opcao_primaria == 4:
            tipo = "professor"
        elif opcao_primaria == 5:
            tipo = "matrícula"
        elif opcao_primaria == 6:
            print("\nVocê saiu do aplicativo...")
            break

        while True:
            opcao_secundaria = menu_secundario()

            if opcao_secundaria == 1:  # Incluir.
                novo_cadastro = realizar_cadastros(tipo.capitalize())
                dados_de_cadastro[tipo].append(novo_cadastro)
                salvar_dados(dados_de_cadastro)

            elif opcao_secundaria == 2:  # Listar.
                listar_cadastros(dados_de_cadastro, tipo)

            elif opcao_secundaria == 3:  # Atualizar.
                editar_cadastros(dados_de_cadastro, tipo)
                salvar_dados(dados_de_cadastro)

            elif opcao_secundaria == 4:  # Excluir.
                excluir_cadastros(dados_de_cadastro, tipo)
                salvar_dados(dados_de_cadastro)

            elif opcao_secundaria == 5:  # Voltar ao menu principal.
                break

if __name__ == "__main__":
    funcao_principal()


