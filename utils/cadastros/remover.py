def remover_contato(id):
    try:
        # Abre o arquivo agenda.txt no modo de leitura
        with open("agenda.txt", "r") as agenda:
            contatos = agenda.readlines()
        
        # Abre o arquivo agenda.txt no modo de escrita
        with open("agenda.txt", "w") as agenda:
            # Mantém apenas os contatos cujo ID não é o fornecido
            encontrado = False
            for contato in contatos:
                id_contato, nome, email, telefone = contato.strip().split(";")
                if id_contato != id:
                    agenda.write(contato)
                else:
                    encontrado = True
            
            if encontrado:
                print("Contato removido com sucesso.")
            else:
                print("Contato não encontrado.")
    except FileNotFoundError:
        print("O arquivo de agenda não foi encontrado.")
