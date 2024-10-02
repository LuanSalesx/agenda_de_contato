# Pesquisar contato
def pesquisar_contato(id):
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
            # Pesquisa o ctt pelo ID
            for contato in contatos:
                id_contato, nome, email, telefone = contato.strip().split(";")
                if int(id_contato) == id:
                    return f"ID: {id_contato}, Nome: {nome}, Email: {email}, Telefone: {telefone}"
                return "Contato não encontrado."
    except FileNotFoundError:
        return "Arquivo não encontrado. Crie um contato primeiro"