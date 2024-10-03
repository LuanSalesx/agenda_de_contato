def listar_contatos():
    try:
        # Abre o arquivo agenda.txt no modo de leitura
        with open("agenda.txt", "r") as agenda:
            # Lê todas as linhas do arquivo
            contatos = agenda.readlines()
            # Verifica se há contatos
            if contatos:
                print("Lista de Contatos:")
                # Para cada linha no arquivo, separa os dados e exibe
                for contato in contatos:
                    id, nome, email, telefone = contato.strip().split(";")
                    print(f"ID: {id}, Nome: {nome}, Email: {email}, Telefone: {telefone}")
            else:
                print("Nenhum contato encontrado.")
    except FileNotFoundError:
        print("O arquivo de agenda não foi encontrado. Crie um contato primeiro.")
