def pesquisar_contato(id):
    try:
        # Abre o arquivo agenda.txt no modo de leitura
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
            # Pesquisa o contato pelo ID
            for contato in contatos:
                id_contato, nome, email, telefone = contato.strip().split(";")
                if id_contato == id:
                    return f"ID: {id_contato}, Nome: {nome}, Email: {email}, Telefone: {telefone}"
            return "Contato não encontrado."
    except FileNotFoundError:
        return "O arquivo de agenda não foi encontrado. Crie um contato primeiro."
