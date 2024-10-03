from utils.cadastros.incluir import incluir_contato
from utils.cadastros.listar import listar_contatos
from utils.cadastros.pesquisar import pesquisar_contato
from utils.cadastros.remover import remover_contato
import os

# Função para gerar o próximo ID único
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

# Menu principal
def menu():
    while True:
        print("\n====== Agenda de Contatos do Luan ======")
        print("(1) Incluir Contato")
        print("(2) Listar Contatos")
        print("(3) Pesquisar Contato")
        print("(4) Remover Contato")
        print("(5) Sair")
        print(40 * "=")

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

        elif opcao == "3":
            id = input("Digite o ID do contato: ")
            print(pesquisar_contato(id))

        elif opcao == "4":
            id = input("Digite o ID do contato a ser removido: ")
            remover_contato(id)

        elif opcao == "5":
            print("Saindo do programa...Fim.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
