def incluir_contato(id, nome, email, telefone):
    # Abre o arquivo agenda.txt no modo de adição
    with open("agenda.txt", "a") as agenda:
        # Adiciona um novo contato
        agenda.write(f"{id};{nome.upper()};{email.upper()};{telefone}\n")
    print("Contato incluído com sucesso!")

