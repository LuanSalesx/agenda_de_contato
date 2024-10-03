def remover_contato(id):
    """
    Função para remover um contato da agenda.

    Args:
        id (int): ID do contato a ser removido.

    Returns:
        None
    """
    try:
        # Abre o arquivo no modo leitura
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
            # Abre o arquivo no modo escrita
        with open("agenda.txt", "w") as agenda:
            # Contatos onde o ID não é fornecido
            contato_encontrado = False
            for contato in contatos:
                id_contato, nome, email, telefone = contato.strip().split(",")
                if id_contato  != id:
                    agenda.write(contato)
                else:
                    contato_encontrado = True
            if contato_encontrado:
                print("Contato removido com sucesso.")
            else:
                print("Contato não encotrado.")
    except FileNotFoundError:
        print("Arquivo de agenda não foi encontrado.")
