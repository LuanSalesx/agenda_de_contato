# Incluir contatos
import os
def incluir(agenda_file, nome, email, telefone):    
    nome = nome.upper()
    email = email.upper()
    telefone = telefone.upper()

    if not os.path.exists(agenda_file):
        open(agenda_file, 'w').close()

    
    with open(agenda_file, 'a') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            contato_data = linha.strip().split(',')
            if contato_data[0] == nome or contato_data[1] == email:
                print(f"ERRO: Contato {nome} já existe na agenda.")
                return
            
    id_contato = len(linhas) + 1
    with open(agenda_file, 'a') as arquivo:
        arquivo.write(f"{id_contato}, {nome}, {email}, {telefone}\n")
        print(f"Contato {nome} incluído com sucesso.")