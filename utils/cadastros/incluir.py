def incluir_contato(id, nome, email, telefone):
    # Abre o arquivo agenda.txt no modo de adição ('a') para não sobrescrever os dados existentes
    with open("agenda.txt", "a") as agenda:
        # Adiciona um novo contato no formato id;nome;email;telefone
        agenda.write(f"{id};{nome.upper()};{email.upper()};{telefone}\n")
    print("CONTATO INCLUÍDO COM SUCESSO!")
