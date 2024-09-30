import os

def incluir_contato(agenda_path, nome, email, telefone):
    nome = nome.upper()
    email = email.upper()
    telefone = telefone.upper()

    if not os.path.exists(agenda_path):
        open(agenda_path, 'w').close()

    with open(agenda_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            contact_data = line.strip().split(',')
            if contact_data[1] == nome or contact_data[2] == email:
                print("Erro: Nome ou email já cadastrado!")
                return

    id_contato = len(lines) + 1  # ID será sempre crescente
    with open(agenda_path, 'a') as file:
        file.write(f"{id_contato},{nome},{email},{telefone}\n")
    print("Contato incluído com sucesso!")
