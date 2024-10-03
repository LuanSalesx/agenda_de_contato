# Listar contatos
def listar_contatos():
    """
    Função para listar todos os contatos na agenda.
    Lê o arquivo agenda.txt e exibe cada contato formatado.
    Caso não haja contatos, exibe uma mensagem informando
    que não há contatos na agenda.
    Returns:
        None
    """
    try:
        # Abre o arquivo agenda.txt
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
