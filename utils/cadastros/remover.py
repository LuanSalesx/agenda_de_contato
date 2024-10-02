def remover_contato(id):
    try:
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
        with open("agenda.txt", "w") as agenda:
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
