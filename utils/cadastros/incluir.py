def incluir_contato(id, nome, email, telefone):
    """
    Função para incluir um novo contato na agenda.

    Args:
        id (int): ID do contato.
        nome (str): Nome do contato.
        email (str): Email do contato.
        telefone (str): Telefone do contato.

    Returns:
        None
    """
    # Abre o arquivo agenda.txt
    with open("agenda.txt", "a") as agenda:
        # Adiciona um novo contato
        agenda.write(f"{id};{nome.upper()};{email.upper()};{telefone}\n")
    print("Contato incluído com sucesso!")