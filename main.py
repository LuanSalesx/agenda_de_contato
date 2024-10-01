import os
from utils.cadastros.incluir import incluir_contato
from utils.cadastros.listar import listar_contatos

def gerar_proximo_id():
    if not os.path.exists("agenda.txt"):
        return 1  # Se o arquivo não existir, o primeiro ID será 1
    with open("agenda.txt", "r") as agenda:
        contatos = agenda.readlines()
        if contatos:
            # Pega o último ID e adiciona 1
            ultimo_id = int(contatos[-1].split(";")[0])
            return ultimo_id + 1
        return 1  # Se o arquivo estiver vazio, o ID será 1

def menu():
    while True:
        print("\n------ Agenda de Contatos ------")
        print("1. Incluir Contato")
        print("2. Listar Contatos")
        print("3. Pesquisar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ").upper()
            email = input("Email: ").upper()
            telefone = input("Telefone: ")

            # Gera um novo ID e inclui o contato
            id = gerar_proximo_id()
            incluir_contato(id, nome, email, telefone)

        elif opcao == "2":
            listar_contatos()